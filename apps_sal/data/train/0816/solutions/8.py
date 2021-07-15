t = int(input())
l = list(map(int,input().split()))
n = int(input())
for _ in range(n):
    t = int(input())
    print(l[t-1])
    del l[t-1]
