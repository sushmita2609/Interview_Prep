# EY

# anagram
from collections import Counter
#
#
# def check_anagram(s1, s2):
#     if len(s1) != len(s2):
#         return False
#
#     str1 = Counter(s1)
#     str2 = Counter(s2)
#     return str1 == str2
#
# s1 = "listen"
# s2 = "lists"
# print(check_anagram(s1, s2))

def first_non_repeating(a):
    k = set()
    for i in a:
        print(a)
        if i in k:
            a = a.replace(i,"")
        else:
            k.add(i)
    return a

a = "nxtxto"
print(first_non_repeating(a))


t = lambda x:x*x
print(t(2))



