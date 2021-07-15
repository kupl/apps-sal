# cook your dish here
n=int(input())
for i in range(n):
    l=[int(i) for i in input().split()]
    if sum(l)==180:print("YES")
    else:print("NO")
