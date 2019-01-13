import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url,headers=headers)
print(response.text)
url = response.text.split('\r\n')
print(url)
for i in url:
    try:
        response = requests.get(i,allow_redirects=False,timeout=3)
        with open('E:/python_wf/{}'.format(i.split('/')[-1]), mode='wb') as f:
            f.write(response.content)
            f.flush()
    except  Exception as e:
        print(e)