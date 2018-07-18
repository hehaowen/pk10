# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class NumberPipeline(object):

    def open_spider(self, spider):
        self.conn = sqlite3.connect('../db.sqlite3')
        self.cur = self.conn.cursor()


    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        insert_sql = 'insert into index_pk10 (qishu,haoma,shijian) values ("{}","{}","{}")'.format(item['qishu'],item['haoma'],item['shijian'])
        self.cur.execute(insert_sql)
        self.conn.commit()
        return item

    def spider_close(self, spider):
        self.conn.close()
