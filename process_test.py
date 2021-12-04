from os import environ as env
from time import sleep
from multiprocessing import Process, Queue

def target_func(q):
    if 'PLAY' in env:
        q.put(f"==> PLAY is: {env['PLAY']}")
    else:
        q.put("==> PLAY is not in environment!")
    for i in range(100):
        q.put(f"child process: {i}")
        sleep(1)

if __name__ == "__main__":
    env['PLAY'] = 'no-time'
    q = Queue()
    p = Process(target=target_func, args=(q,))
    p.start()
    input("Please press <Enter> to finish main process.")
    p.terminate()
    p.join()
    while not q.empty():
        print(q.get())
    print("main process finished.")
