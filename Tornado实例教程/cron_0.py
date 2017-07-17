from tornado import ioloop, gen
@gen.coroutine
def Count():
    print ('1 second has gone.')

if __name__ == '__main__':
    ioloop.PeriodicCallback(Count, 1000).start()
    ioloop.IOLoop.current().start()