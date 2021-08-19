case = int(input())
for c in range(case):
    (l, k) = map(int, input().split())
    if l < k:
        print('Case {}:'.format(c + 1), 0)
    else:
        n = l - k + 1
        sum = n * (n + 1) // 2
        print('Case {}:'.format(c + 1), sum)
