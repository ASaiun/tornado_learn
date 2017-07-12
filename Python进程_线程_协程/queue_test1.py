# import Queue
#
# q = Queue.Queue(maxsize=0)
#
# q.join()
# q.qsize()
# q.empty()
# q.full()
# q.put(item, block=True, timeout=None)
# q.get(block=True, timeout=None)
# q.put_nowait(item)
# q.get_nowait()
#
#


import Queue
import threading
message = Queue.Queue(10)

def producer(i):
    while True:
        message.put(i)

def consumer(i):
    while True:
        msg = message.get()
        print msg

for i in range(12):
    t = threading.Thread(target=producer, args=(i, ))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer, args=(i,))
    t.start()
