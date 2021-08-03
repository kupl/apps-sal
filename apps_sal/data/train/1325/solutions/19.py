tc = int(input())
while(tc > 0):
    a = list(map(int, input().split()))
    a1 = a[3] - a[1]
    a2 = a[3] - a[2]
    a3 = a[3] - a[0]
    print(a1, a2, a3)
    tc = tc - 1
