'''
n=int(input())
a=list(map(int,input().split()))
sum=0
c=0
for i in range(len(a)):
    sum+=a[i]
    #print(sum)
    if sum==0:
     c+=1
     sum=a[i]
print(c)

'''
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
res = 0
# lst=[a[0]]
sum = 0
lst = []
# print(lst)
# print(lst[-1])
for i in range(n):
    sum += a[i]
    lst.append(sum)
# print(lst)
count = Counter(lst)
# print(count[0])
# print(count.values())
count[0] += 1
# print(count[0])
# print(count.values())
for i in list(count.values()):
    res += i * (i - 1) // 2
print(res)
