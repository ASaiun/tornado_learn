from multiprocessing import Process

def func(name):
    print ('hello', name)

if __name__ == '__main__':
    p = Process(target=func, args=('test',))
    p.start()
    p.join()