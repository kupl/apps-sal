t = int(input())
for i in range(0, t):
    n = int(input())
    l = list(map(int, input().split()))
    if n == 1:
        print(l[0])
    else:
        print(max(l[n - 1], l[0]))
