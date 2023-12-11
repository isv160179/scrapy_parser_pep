from datetime import datetime
from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
PEP_NUMBER_NAME = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'
BASE_DIR = Path(__file__).parent.parent / 'results'
FILE_NAME = 'status_summary_{}.csv'.format(
    datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
)
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
ALLOWED_DOMAINS = 'peps.python.org'