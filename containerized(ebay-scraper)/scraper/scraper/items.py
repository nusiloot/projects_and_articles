# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_title = scrapy.Field()
    product_item_num = scrapy.Field()
    product_availability = scrapy.Field()
    product_total_sold = scrapy.Field()
    product_price = scrapy.Field()
    product_currency = scrapy.Field()
    product_rating = scrapy.Field()
    number_of_reviews = scrapy.Field()