for _ in range(int(input())):
    (l, k) = map(int, input().split())
    if k <= l:
        n = l - k + 1
        res = n * (n + 1) // 2
    else:
        res = 0
    print(f'Case {_ + 1}: {res}')
