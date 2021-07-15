# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    if a[0]>a[-1]:
        print(a[0])
    else:
        print(a[-1])
