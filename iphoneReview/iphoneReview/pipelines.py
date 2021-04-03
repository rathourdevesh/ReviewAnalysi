# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class IphonereviewPipeline:
    def __init__(self):
        self.conn = sqlite3.connect("reviewData.db")
        self.curr = self.conn.cursor()

    def process_item(self, item, spider):
        self.curr.execute("insert into reviewDataTable(reviewText) values (?)",(
            #item['ReviewTitle'][0],
            item['ReviewText'][0],
            #item['StyleName'][0],
            #item['Colour'][0],
            #item['VrfFlag'][0]
        ))
        self.conn.commit()
        
        return item
