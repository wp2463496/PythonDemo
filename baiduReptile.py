import urllib.request

import re

import os

# 全局取消证书验证
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 导入lxml
from lxml import etree

openUrls = ["https://baike.baidu.com/item/python/407313"]

count = 0

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

def task():
	baseUrl = 'https://baike.baidu.com'

	global count

	url = openUrls[count]

	response = urllib.request.urlopen(url).read().decode()

	html = etree.HTML(response)

	texts = html.xpath('//div[@class="lemma-summary"]//div[@class="para"]/a/text()') 

	urls = html.xpath('//div[@class="lemma-summary"]//div[@class="para"]/a/@href') 

	for urlStr in urls:
		openUrl = baseUrl + urlStr
		openUrls.append(openUrl);

	print(texts)

	print(openUrls)

	file_path = GetDesktopPath() + "/baiduReptile.txt"

	file = open(file_path, "a+")

	n = 0

	for value in texts:
		file.write(texts[n] + ":")
		file.write('\n')
		file.write(openUrls[n])
		file.write('\n')
		file.write('\n')
		n += 1

	file.write('\n')

	file.close()

	count += 1

task()

while openUrls[count]:
	task()
	if count >= 100:
		break

