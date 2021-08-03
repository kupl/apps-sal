t = int(input())
sum = 0
for _ in range(t):
    s, n, k, r = map(int, input().split())
    if r == 1:
        k = s - n * k
    else:
        k = s - k * ((r**n - 1) // (r - 1))
    sum += k
    if k < 0:
        print('IMPOSSIBLE', -k)
    else:
        print('POSSIBLE', k)
if sum < 0:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
