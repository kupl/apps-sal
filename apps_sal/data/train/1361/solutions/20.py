# cook your dish here
list0 = list(map(int, input().split()))
n = list0[0]
k = list0[1]
list1 = list(map(int, input().split()))
M = 1000000007
for j in range(k):
    for i in range(n - 1):
        list1[i + 1] = list1[i + 1] + list1[i]
for i in list1:
    print(i % M, end=" ")
