from os import environ as env
from time import sleep
from multiprocessing import Process

def target_func():
    if 'PLAY' in env:
        print(f"==> PLAY is: {env['PLAY']}")
    else:
        print("==> PLAY is not in environment!")
    for i in range(100):
        print(f"child process: {i}")
        sleep(1)

env['PLAY'] = 'Great'
p = Process(target=target_func, args=(,))
p.start()

input("Please press <Enter> to finish main process.")
p.terminate()
p.start()
