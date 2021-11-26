import bjoern
from urllib.parse import unquote

L = 10

D = {}

def app(env, start_response):
    path_info = env['PATH_INFO']
    path_list = path_info.split('/')
    path_list = [s for s in path_list if s]
    msg = None
    if len(path_list) > 1:
        msg = unquote('/'.join(path_list[1:]))
    name = path_list[0]
    if name not in D:
        value_list = []
        D[name] = value_list
    value_list = D[name]
    if msg is None: # read
        if value_list:
            start_response('200 OK', [])
            value = value_list.pop(0)
            return value
        else:
            start_response('400 no message!', [])
            return b''
    else: # write
        if len(value_list) >= L: # message full!
            start_response('400 message full! (max 10 messages).', [])
            return b''
        else:
            start_response('200 OK', [])
            msg_b = msg.encode()
            value_list.append(msg_b)
            return b'OK: ' + msg_b

bjoern.run(app, '0.0.0.0', 8000)
