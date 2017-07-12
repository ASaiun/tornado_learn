#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from multiprocessing import Array, Value,  Process
#
# def func(a,b):
#     a.value = 3.333333333333333
#     for i in range(len(b)):
#         b[i] = -b[i]
#
# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(11))
#
#     c = Process(target=func, args=(num, arr))
#     d = Process(target=func, args=(num, arr))
#
#     c.start()
#     d.start()
#
#     c.join()
#     d.join()
#
#     print (num.value)
#     for i in arr:
#         print(i)

#并没有得到预期的效果
# 3.1415927
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]



from multiprocessing import Array, Value, Process


def func(a, b):
    a.value = 3.333333333333333
    for i in range(len(b)):
        b[i] = -b[i]


if __name__ == "__main__":
    num = Value('d', 0.0)
    arr = Array('i', range(11))

    c = Process(target=func, args=(num, arr))
    d = Process(target=func, args=(num, arr))
    c.start()
    d.start()
    c.join()
    d.join()

    print(num.value)
    for i in arr:
        print(i)