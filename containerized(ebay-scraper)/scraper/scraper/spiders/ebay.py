from types import NoneType
import scrapy
from scraper.items import ScraperItem
import time

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    custom_settings = {
        "FEEDS":{"scraped_data.csv":{"format":"csv"}}
        }

    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/str/fixdeals?_fcid=1&_pgn=1']

    def parse(self, response):

        # Fetch all the item URLs from start_urls response
        itemUrls= response.xpath('//a[contains(@class, "str-item-card__link")]/@href').getall()
        # Iterating through all URLs to get reponses and passing to parse_content class
        for url in itemUrls:
            time.sleep(1)
            yield scrapy.Request(url= url, callback= self.parse_content, dont_filter=True)
        
        # Extracting the URL for next page and passing again to parse function
        for page_num in range(2, 32):
            nextPage= f'https://www.ebay.com/str/fixdeals?_fcid=1&_pgn={page_num}'
            time.sleep(1)
            yield response.follow(nextPage, self.parse)
        
    def parse_content(self, response):

        item= ScraperItem()

        # STRING
        item["product_title"]= response.xpath('//*[@id="LeftSummaryPanel"]/div[1]/div[1]/div/h1/span/text()').get()

        # STRING
        item["product_item_num"]= response.xpath('//*[@id="readMoreDesc"]/div/div/div[2]/div/div/div/span[2]//text()').get()

        # Integar
        item["product_availability"]= int(self.Multiple_StringToInt(response.xpath('//*[@id="qtySubTxt"]/span/text()').get(), 0))

        # Integar
        item["product_total_sold"]= int(self.Multiple_StringToInt(response.xpath('//*[@id="mainContent"]/form/div[1]/div[3]/div[2]/div/div[1]/span[2]/span[3]/a//text()').get(), 0))

        price= self.Multiple_StringToInt(response.xpath('//*[@id="prcIsum"]/text()').get(), 1)
        # Float
        item["product_price"]= float(self.currToPrice(price))

        # Currency Symbol
        item["product_currency"]= self.currOnly(price)

        # float
        item["product_rating"]= float(self.Multiple_StringToInt(response.xpath('//*[@id="rwid"]/div[@class="reviews-left"]/div[@class="ebay-content-wrapper"]/span[@class="ebay-review-start-rating"]//text()').get(), 0))
        
        # Integar
        item["number_of_reviews"]= int(self.Multiple_StringToInt(response.xpath('//*[@id="_rvwlnk"]//text()').get(), 0))

        yield item

    def Multiple_StringToInt(self, xpath, num):
        try:
            if xpath is not NoneType:
                return xpath.split()[num]
        except:
            return 0

    def currToPrice(self, usprice):
        try:
            if len(usprice) > 1:
                return float(usprice[1:])
        except:
            return usprice

    def currOnly(self, usprice):
        try:
            if len(usprice) > 1:
                return usprice[0]
        except:
            return usprice