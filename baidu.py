import urllib.request

import re

import os

url = r"http://wwww.baidu.com"

response = urllib.request.urlopen(url).read().decode()

pat = r"<title>(.*?)</title>"

data = re.findall(pat, response)

print(data)

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

file_path = GetDesktopPath() + "/baiduout.txt"

file = open(file_path, "a+")

text = ''

for strs in data:
   text += strs + ";"

text = text[0: len(text)-1:]

file.write(text)

file.write('\n')

file.close()