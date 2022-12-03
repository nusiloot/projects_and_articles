from types import NoneType
import scrapy
from amazon_scraping.items import AmazonscraperItem
import time

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    kw= input("Write Keyword: ")
    start_urls = [f'https://www.amazon.com/s?k={kw}']

    def parse(self, response):

        # From Main Page to Product Listing
        for href in response.xpath("//a[contains(@class, 'a-link-normal s-no-outline')]/@href").extract():
            update_href= "https://www.amazon.com" + str(href)
            time.sleep(2)
            yield scrapy.Request(url= update_href, callback= self.parse_dir_content)

        # For scraping all main pages
        #Range 7 because amazon go upto maximum of 7 pages

        for page in range(2, 8):
            next_page= f"https://www.amazon.com/s?k=oneodio&page={page}"
            time.sleep(1)
            yield response.follow(next_page, self.parse)

    def parse_dir_content(self, response):
        item= AmazonscraperItem()
        
        # Title - String
        try:
            item['title']= response.xpath('//*[@id="productTitle"]//text()').get().strip()
        except:
            item['title']= "NULL"
        
        #Brand Name - String
        if type(response.xpath('//*[@id="bylineInfo"]/text()').get()) is not NoneType:
            item['brand']= response.xpath('//*[@id="bylineInfo"]/text()').get()
        else:
            item['brand']= "NA"

        # ASIN - String
        if type(response.xpath('//*[@id="ASIN"]/@value').get()) is not NoneType:
            item['asin']= response.xpath('//*[@id="ASIN"]/@value').get()
        else:
            item['asin']= "NA"

        # Variation Price - String
        if type(response.xpath('//*[@id="newAccordionCaption_feature_div"]/div/span//text()').get()) is not NoneType:
            item['var_price']= response.xpath('//*[@id="corePrice_feature_div"]/div/div/span/span[1]//text()').get()
        elif type(response.xpath('//*[@id="corePrice_feature_div"]/div/div/span/span[1]//text()').get()) is NoneType and type(response.xpath('//*[@id="corePrice_feature_div"]/div/span/span[1]//text()').get()) is NoneType and type(response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]/text()').get()) is NoneType:
            item['var_price']= "NULL"
        else:
            item['var_price']= response.xpath('//*[@id="corePrice_feature_div"]/div/span/span[1]//text()').get()
            
        # Availability - String
        if type(response.xpath('//*[@id="availability"]/span/text()').get()) is not NoneType:
            item['available_status']= response.xpath('//*[@id="availability"]/span/text()').get().strip()
        else:
            item['available_status']= "Out of stock"

        # Total_Feedbacks - String
        if type(response.xpath('//*[@id="acrCustomerReviewText"]/text()').get()) is not NoneType:
            item['review_count']= response.xpath('//*[@id="acrCustomerReviewText"]/text()').get()
        else:
            item['review_count']= "NULL"

        # Review Rating -  String
        if type(response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]//text()').get()) is not NoneType:
            item['review_rating']= response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]//text()').get()
        else:
            item['review_rating']= "NULL"

        # Variation Type - String
        try:
            item['variation_type']= response.xpath('//*[@id="variation_color_name"]/div/label/text()').get().strip()
        except:
            item['variation_type']= "NULL"

        # No. of Variations - Integar
        if len(response.xpath('//*[@id="variation_color_name"]/ul/text()').getall()) != 0:
            item['num_variations']= len(response.xpath('//*[@id="variation_color_name"]/ul/text()').getall()) - 1 
        else:
            item['num_variations']= 0

        # Variation Colour - String
        try:
            item['var_color']= response.xpath('//*[@id="variation_color_name"]/div/span/text()').get().strip()  
        except:
            item['var_color']= "NULL"

        yield item