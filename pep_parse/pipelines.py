import csv

from pep_parse.settings import FILE_NAME, BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = {}

    def process_item(self, item, spider):
        status = item['status']
        self.total[status] = self.total.setdefault(status, 0) + 1
        return item

    def close_spider(self, spider):
        self.total['Total'] = sum(self.total.values())
        file_path = BASE_DIR / FILE_NAME
        file = csv.writer(open(file_path, 'w'))
        file.writerow(['Статус', 'Количество'])
        file.writerows(self.total.items())
