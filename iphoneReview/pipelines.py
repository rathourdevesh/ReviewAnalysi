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
        for i in range(0,len(item)-1):
            self.curr.execute("insert into reviewDataTable(Title,reviewText,StyleName,Colour,VrfFlag,Rating) values (?,?,?,?,?,?)",(
                item['ReviewTitle'][i],
                item['ReviewText'][i],
                item['StyleName'][i],
                item['Colour'][i],
                item['VrfFlag'][i],
                item['Rating'][i]

            ))
            self.conn.commit()
        
        return item
