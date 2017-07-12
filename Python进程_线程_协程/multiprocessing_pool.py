from multiprocessing import Pool

import time

# def f1(i):
#     time.sleep(0.5)
#     print (i)
#     return i + 100
#
# if __name__ == '__main__':
#     pool = Pool(5)
#     for i in range(1, 31):
#         pool.apply(func=f1, args=(i, ))

def f1(i):
    time.sleep(0.5)
    print (i)
    return i + 100

def f2(arg):
    print(arg)

if __name__ == '__main__':
    pool = Pool(5)

    for i in range(1, 31):
        pool.apply_async(func=f1, args=(i, ), callback=f2)

    pool.close()
    pool.join()
