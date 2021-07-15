# cook your dish here
n = int(input())
while n>0:
    s = list(map(int,input().strip()))
    print(sum(s))
    n = n-1
