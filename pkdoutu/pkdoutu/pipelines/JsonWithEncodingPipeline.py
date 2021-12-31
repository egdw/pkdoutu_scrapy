import json
import codecs
import os

# 将Unicode码转换为中文
class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line+',')
        return item

    def close_spider(self, spider):
        self.file.seek(-1, os.SEEK_END)
        self.file.truncate();
        self.file.write(']')
        self.file.close()