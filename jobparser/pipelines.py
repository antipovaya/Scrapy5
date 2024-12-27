# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from pprint import pprint

class JobparserPipeline:
    # def __init__(self):
    #     self.vacancys = []
    def process_item(self, item, spider):
        # all_vacancys = []
        # self.vacancys.append(item)
        # with open('vacancys.json', 'a') as f:
        #     json.dump(list(self.vacancys), f)
        # pprint(self.vacancys)
        # print()
        return item
