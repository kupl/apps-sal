VQ = 'UAMmSs'
n = int(input())
a = list(map(int, input().split()))
for _ in range(int(input())):
    (q, x, y) = input().split()
    if q not in VQ:
        print('!!!')
        continue
    if q == 'U':
        a[int(x) - 1] = int(y)
        continue
    l = int(x) - 1
    r = int(y)
    if q == 'A':
        print(sum(a[l:r]))
        continue
    if q == 'M':
        print(max(a[l:r]))
        continue
    if q == 'm':
        print(min(a[l:r]))
        continue
    s = sorted(set(a[l:r]))
    if len(s) < 2:
        print('NA')
    else:
        print(s[1] if q == 's' else s[-2])
