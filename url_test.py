from urllib.request import urlopen
from urllib.parse import quote, unquote

base_url = 'http://bitfun.mooo.com:8000'

def check(fd):
    status = fd.getcode()
    if status == 200: return
    else:
        raise Exception(f"Error: {status} - {fd.read(10000)}")

def read(name):
    fd = urlopen(base_url + '/' + name)
    check(fd)
    msg = fd.read(1024).decode()
    return msg

def write(name, msg):
    assert len(msg) < 1024
    assert isinstance(msg, str)
    msg_q = quote(msg)
    fd = urlopen(base_url + '/' + name + '/' + msg_q)
    check(fd)

# Below are test code
name_list = ['David', 'Chris', 'Sam']

for i in range(10):
    for name in name_list:
        write(name, f"message {i} for {name}.")

for name in name_list:
    for i in range(10):
        msg = read(name)
        if msg != f"message {i} for {name}.":
            print(f"Error: {msg} -- should be: message {i} for {name}")
        else:
            print(f"{name} {i} OK.")
