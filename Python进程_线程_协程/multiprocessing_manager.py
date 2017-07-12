from multiprocessing import Process, Manager

def f(d, l):
    d["name"] = "test1"
    d["age"] = 18
    d["Job"] = "pythoner"
    l.reverse()

if __name__ == '__main__':
    with Manager() as man:
        d = man.dict()
        l = man.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
