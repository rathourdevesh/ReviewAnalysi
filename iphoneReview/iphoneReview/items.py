# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class IphonereviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ReviewTitle = scrapy.Field()
    ReviewText = scrapy.Field()
    StyleName = scrapy.Field()
    Colour = scrapy.Field()
    VrfFlag = scrapy.Field()
    stylenew = scrapy.Field()
    Rating = scrapy.Field()
    
