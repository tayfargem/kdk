"""
KDK Karar Verilerini İnternetten Alma Modülü

https://kararlar.ombudsman.gov.tr/Arama/Index

"""
import requests
import pandas as pd
from data.kdk_constant import url, headers, data_def

# set range to read
data = data_def
data['start'] = "0"
data['length'] = "10349"

# https://stackoverflow.com/a/65352348
response = requests.post(
    url, headers=headers, data=data
)

resp_json = response.json()

df = pd.DataFrame.from_dict(resp_json['data'])

df.to_csv("kdk_all_data.csv", index=False)

# references and tools
#
# https://www.urldecoder.io/
# https://codebeautify.org/htmlviewer
# https://stackoverflow.com/a/1260846
# import requests
# from scrapy import Selector
# from scrapy.crawler import CrawlerProcess
