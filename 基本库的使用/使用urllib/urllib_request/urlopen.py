import urllib.request
import urllib.parse
import urllib.error
import socket

# 利用最基本的urlopen()方法，可以完成最基本的简单网页的GET请求抓取。

# 如果想给链接传递一些参数，该怎么实现呢？

# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

# data参数
# data参数是可选的。如果要添加该参数，并且如果它是字节流编码格式的内容，即bytes类型，则需要通过bytes()方法转化
# 另外，如果传递了这个参数，则它的请求方式不再是GET方式，而是POST方式

# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
# response = urllib.request.urlopen(' http://0.0.0.0:80/post', data=data)
# print(response.status)
# print(response.read().decode('utf-8'))

# 这里我们传递了一个参数word, 值是hello。它需要被转码成bytes(字节流)类型。
# 其中转字节流采用了bytes()方法，该方法的第一个参数需要是str(字符串)类型，
# 需要用urlLib.parse模块里的urlencode()方法将参数字典化为字符串；第二个参数指定编码格式。

# timeout参数
# timeout参数用来设置超时时间，单位未秒，意思就是如果请求超出了设置的这个时间，还没有得到响应，就会抛出异常。
# 如果不指定该参数，就会使用全局默认时间。

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")

# 其他参数
# context, 必须是ssl.SSLContext类型，用来指定SSL设置
# cafile和capath这两个参数分别指定CA证书和它的路径，这两个参数在强求HTTPS链接时会有用。
# cadefault参数已经别弃用

