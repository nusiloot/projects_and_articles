from scraper.spiders.ebay import EbaySpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# CALLING SPIDER TO CRAWL
def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(EbaySpider)
    process.start() # the script will block here until the crawling is finished

if __name__ == "__main__":
    main()