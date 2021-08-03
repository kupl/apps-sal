n = int(input())

for _ in range(n):
    l = int(input())
    t = map(int, input().split())
    accumm = [0] * 8
    for i in t:
        accumm[i - 1] += 1
    print(min(accumm))
