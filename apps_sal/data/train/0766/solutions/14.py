t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    a = l[0]*l[1]
    b = l[-1]*l[-2]
    print(b,a)

