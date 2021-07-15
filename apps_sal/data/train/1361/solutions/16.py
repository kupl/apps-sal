# cook your dish here
from itertools import accumulate
list0=list(map(int,input().split()))
n=list0[0]
k=list0[1]
list1=list(map(int,input().split()))
list2=list1[0:]
M = 1000000007
for j in range(k):
    list1=list(accumulate(list1))
for i in list1:
    print(i%M,end=" ")
