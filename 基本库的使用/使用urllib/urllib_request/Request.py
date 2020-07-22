# 如果请求需要加入Header等信息，就可以利用更强大的Request类来构建。
from urllib import  request, parse

# request = urllib.request.Request("https://python.org")
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# 第一个参数url用于请求URL，这是必传参数，其他都是可选参数
# 第二个参数data，如果要传，必须传bytes（字节流）类型的。如果它是字典，可以先用urllib.parse模块里的urlencode()编码
# 第三个参数header是一个字典，它就是请求头，我们可以在构造请求时通过headers参数直接构造，
# 也可以通过调用请求实例的add_header()方法添加。
# 添加请求头最常用的用法是通过修改User-Agent来伪装浏览器。
# 第四个参数origin_req_host指的是请求方的host名称或者IP地址
# 第五个参数unverifiable表示这个请求是否是无法验证的，默认是False,意思就是说用户没有足够的权限来选择接收这个请求的结果。
# 例如，我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，这时unverifiable的值就是True.
# 第六个参数method是一个字符串，用来指示请求使用的方法，比如GET、POST和PUT等。


url = 'http://0.0.0.0:80/post'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Host': 'httpbin.org'
}

dict = {
    'name':'Alex'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')

req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36')
response = request.urlopen(req);
print(response.read().decode('utf-8'))
