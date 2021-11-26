import urllib.request
fd = urllib.request.urlopen('http://bitfun.mooo.com:8000')
message = fd.read(1000)
print(message)
