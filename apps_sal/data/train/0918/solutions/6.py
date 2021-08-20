t = int(input())
for i in range(1, t + 1):
    n = int(input())
    ans = 2 ** 33
    if n < 33:
        ans = 1
        for j in range(1, n + 1):
            ans = ans * 2
    print('Case {}: {}'.format(i, ans - 1))
