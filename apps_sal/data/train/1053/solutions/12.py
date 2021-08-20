t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    print(x.index(1))
