# import asyncio,sys,time
# @asyncio.coroutine
# def hello():
#     time.sleep(3)
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(2)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(asyncio.wait([hello() for i in range(3)]))
# loop.close()
#

test_dict ={"qq":"ww"}
test = [1,2,test_dict]

test_list_1 = [1,[1,1,2017101,2017111,2017121],[1,11,2017201,2017211,2017221],[1,21,2017301,2017311,2017321],[1,[1,0]]]

print(test_list_1[4][1][1])
# print(test[2].get("qq"))