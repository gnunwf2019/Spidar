import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
response = requests.get('http://www.17k.com/list/2933095.html',headers=headers)
response.encoding = "utf8"
HTML = response.text
# print(HTML)
regex = re.compile('.*?<a target=\"_blank\" href=\"(.*html)\" title=.*')
#regex = re.compile('.*?if\(!strLink\){document\.write\(\'<a href="\.(.*shtml)".*\'\)}')
result = regex.findall(HTML)
# print(result)
url = ['http://www.17k.com' + i for i in result]
# print(url)
for i in url:
    response = requests.get(i)
    response.encoding = 'utf-8'
    title = re.findall('<h1>\n(.*)</h1>', response.text, re.S)
    content = re.findall('&#12288;&#12288;(.*?)<br /><br />', response.text)
    temp = title + content
    temp_= []
    for q in temp:
        temp_.append(q + '\r\n')
    with open('E:/python_wf/{}.txt'.format(i.split('/')[-1]), mode='w') as f:
        f.writelines(temp_)
        f.flush()
