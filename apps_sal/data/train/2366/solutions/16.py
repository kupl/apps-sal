Q = int(input())
for q in range(Q):
    n = int(input())
    arr = list(map(int, input().split()))

    minimal = 1e9
    bad = 0
    for i in arr[::-1]:
        if i < minimal:
            minimal = i
        if i > minimal:
            bad += 1

    print(bad)

