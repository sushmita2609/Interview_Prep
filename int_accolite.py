# accolite1
# print upto 10 prime numbers
#1 2 3 5 7
def prime_nums(num):
    if num < 2:
        return
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return
    print(num)

n=10
for i in range(n+1):
    prime_nums(i)

from collections import Counter


#anagram check
#Listen → Silent, Earth → Heart

def check_anagram(str1,str2):
    st1 = str1.replace(" ","")
    st2 =str2.replace(" ", "")
    n = Counter(st1)
    n1 = Counter(st2)
    if n == n1:
        return True
    else:
        return False

str1= "a gentleman"
str2="elegant man"
print(check_anagram(str1,str2))