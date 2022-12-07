# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from datetime import datetime
import logging
from itemadapter import ItemAdapter
import psycopg2

class WorldometersPipeline:
    
    # CONNECTING SPIDER WITH THE POSTGRES DATABASE
    def open_spider(self, spider):
        logging.info("connecting with database")
        
        # CREATING CONNECTION
        self.connection= psycopg2.connect(
            host= 'local-host or IPv4 address',
            user= 'user-name',
            password= 'password',
            database= 'database-name'
        )
        # CREATING CURSOR
        self.curr= self.connection.cursor()

    def process_item(self, item, spider):
        
        # CREATING TABLE IN DATABASE
        self.curr.execute(''' 
        CREATE TABLE IF NOT EXISTS world_population(
            scraped_date TIMESTAMP,
            year DATE NOT NULL PRIMARY KEY,
            population INT8,
            yearly_perc_change DECIMAL,     
            yearly_change INT8,
            migrants DECIMAL,
            median_age DECIMAL, 
            fert_rate DECIMAL,
            density INT, 
            urban_pop_perc DECIMAL,
            urban_pop INT8,
            perc_pop_worldwide DECIMAL,
            world_pop INT8, 
            global_rank INT2
        ) ''')

        # INSERTING VALUES INTO THE DATABASE
        self.curr.execute('''
            INSERT INTO world_population (
                scraped_date, 
                year, 
                population, 
                yearly_perc_change, 
                yearly_change, 
                migrants, 
                median_age, 
                fert_rate, 
                density, 
                urban_pop_perc, 
                urban_pop, 
                perc_pop_worldwide, 
                world_pop, 
                global_rank
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
                datetime.today().strftime("%Y-%m-%d %A"),
                item['year'], 
                item['population'], 
                item['yearly_perc_change'], 
                item['yearly_change'], 
                item['migrants'], 
                item['median_age'], 
                item['fert_rate'], 
                item['density'], 
                item['urban_pop_perc'], 
                item['urban_pop'], 
                item['perc_pop_worldwide'], 
                item['world_pop'], 
                item['global_rank']
        ))

        self.connection.commit()
        logging.info("Transfering Data to postgres Database")
        return item

    # CLOSING THE SPIDER 
    def close_spider(self, spider):
        # CLOSING CURSOR
        self.curr.close()
        logging.info("closing connections")
        #CLOSING CONNECTION
        self.connection.close()