v = int(input())
for i in range(0, v):
    s = list(map(int, input().split()))
    print(max(s), sum(s))
