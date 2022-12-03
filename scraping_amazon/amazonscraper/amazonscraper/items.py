# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ebay_title= scrapy.Field()
    ebay_brand= scrapy.Field()
    ebay_item_num= scrapy.Field()
    ebay_var_price= scrapy.Field()
    ebay_available_status= scrapy.Field()
    ebay_seller_review_count= scrapy.Field()
    ebay_review_rating= scrapy.Field()
    ebay_variation_type= scrapy.Field()
    ebay_num_variations= scrapy.Field()
    ebay_var_color= scrapy.Field()
