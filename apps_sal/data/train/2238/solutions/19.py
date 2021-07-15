n = int(input())
for kase in range(n):
    l, r = map(int, input().split())
    bit = 0
    while l | (1 << bit) <= r:
        l = (l | (1 << bit))
        bit += 1
    print(l)
