def get(l, r):
    while l | l + 1 <= r:
        l |= l + 1
    return l


q = int(input())
for i in range(q):
    (l, r) = list(map(int, input().split()))
    print(get(l, r))
