n = int(input())

target = [x for x in range(n)]
for i in range(n):
    v = list(map(int, input().split()))

    if sorted(v) == target:
        print(' '.join([str(x) if x != 0 else str(n) for x in v]))
        return
