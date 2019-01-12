import urllib.request
import urllib.parse
def main():
    headers = {            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    request= urllib.request.Request(url='http://www.17k.com/chapter/2933095/36699279.html',method="GET")
    response = urllib.request.urlopen(request)
    HTML=response.read().decode('utf8')
    print(HTML)
    with open("/home/suibian/Desktop/py/345.txt",mode='w') as f:
        f.write(HTML)
main()
