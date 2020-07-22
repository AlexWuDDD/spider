import urllib.request

# 提供了最基本的构造HTTP请求的方法，利用它可以模拟浏览器的一个请求发起过程
# 同时它还有处理授权验证（authenticaton）, 重定向（redirection）、浏览器Cookies以及其他内容

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))

# 利用type()方法输出相应的类型
# print(type(response))

# 例如,调用 read ()方法可以得到返回的网页内容,调用 status 属性可以得到返回结果的状态码 ,
# 如 200 代表请求成功, 404 代表网页未找到等 。

print(response.status)
print(response.getheaders())
print(response.getheader("Server"))

# 可见前两个输出分别输出了响应的状态码和响应的头信息，最后一个输出通过调用getheader()
# 并传递一个参数Server获取了响应头中的值，结果是nginx。


