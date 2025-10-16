#ACCION LABS

# list comprehension to print square of all nums
a = [1,2,3,4,5,6,7,8,9,10]
k = [ele*ele for ele in a]

# list comprehension to print if even else num
k = ["*" if ele%2==0 and ele%3==0 else ele for ele in a]

print(k)

# count the frequency of each chars in string
def count_ch(a):
    d = {}
    for i in a:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
        # d[i] = d.get(i,0) +1
    return d
a= "sushmita ghosh"
print(count_ch(a))

# with open ("abc.py", "r") as f:
#     f.read()



a= "sushmita ghosh"
w = {}
w = {i:a.count(i) for i in a}
print(w)


