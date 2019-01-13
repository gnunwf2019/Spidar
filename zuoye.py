import requests
import re
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
response = requests.get(url,headers=headers)
print(response.text)
# a = """
# http://farm1.static.flickr.com/73/159221304_61ee550d56.jpg
# http://farm1.static.flickr.com/44/157910578_1c1eef88c4.jpg
# """
reg = '(htt[p|ps]://.*)\r.*'
url = re.findall(reg,response.text)
print(url)
for i in url:
    try:
        response = requests.get(i, allow_redirects=False,timeout = 3)
        with open('E:/python_wf/venv/{}.jpg'.format(i), mode='wb') as f:
            f.write(response.content)
            f.flush()
    except Exception as e:
        print(e)