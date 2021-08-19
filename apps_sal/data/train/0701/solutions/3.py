for a in range(int(input())):
    (N, k) = map(int, input().split())
    c = list(map(lambda b: k ** b, list(map(int, input().split()))))
    total_sum = sum(c)
    i = 0
    for e in range(N):
        i = i + c[e]
        if i > total_sum - i:
            f = e - 1
            break
    if sum(c[0:f + 2]) == sum(c[f + 2:]):
        print(f + 2)
    elif sum(c[0:f + 2]) >= sum(c[f + 1:]):
        print(f + 1)
    else:
        print(f + 2)
