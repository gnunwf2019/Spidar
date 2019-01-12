import requests
response = requests.get("http://www.baidu.com")
print(response.text)  #huoquwangye yuandaima 
print(response.headers)
print(response.status_code)
print(type(response.headers))
# 也可以加入请求头的方式,去伪装成浏览器
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#liulanqi de biaizhi
response = requests.get('http://www.baidu.com',headers=headers)
print(response.text)