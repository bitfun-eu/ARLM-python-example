from os import environ as env

# env is a dictionary, dump all contents

def dump(e):
    for k in env:
        print(f"--> {k}: {env[k]}")
 
dump(env)

input('Please press <Enter> to continue ...')
# modify/create a environment variable
env['PLAY'] = 'OK'
env['PLAY'] = 'NO'

dump(env)
