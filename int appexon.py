# import time
#
#
# def deco(func):
#     def wrapper(*args, **kwargs):
#         start =  time.time()
#         res =  func(*args, **kwargs)
#         end = time.time()
#         print("Time taken:", end-start)
#         return res
#     return wrapper
#
#
# @deco
# def add(a,b):
#     return a+b
#
# add(3,6)

class example:
    def __enter__(self, file):
        c = file.open()
        return c
    def __exit__(self, file):
        c = file.close()
        return c

with example("abc.txt") as f:
    f.read()

