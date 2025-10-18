# capegemini

# #decorator
def deco(func):
    def wrapper():
        print("before function")
        res = func()
        print("After function")
        return res
    return wrapper

@deco
def print_hello():
    print("Hello")

print_hello()



#sort students details based on score
def sort_student_details(l):
    for i in range(len(l)):
       for j in range(i+1, len(l)):
           if l[i]['score'] > l[j]['score']:
               l[i]['score'] , l[j]['score'] = l[j]['score'] , l[i]['score']
    return l

l = [{'student':'A','score':65},{'student':'E','score':40},{'student':'D','score':95},{'student':'B','score':88},{'student':'C','score':56}]
print(sort_student_details(l))

l.sort(key=lambda x:x['score'])
print(l)



# generator
# def print_val(n):
#     for i in range(n):
#         yield i
#
# j = print_val(5)
# print(next(j))
# print(next(j))
# print(next(j))


