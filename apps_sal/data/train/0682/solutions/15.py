(n, a) = (int(input()), [0] + list(map(int, input().split())))
(l, r) = (1, n)
while l <= n and a[l] == l:
    l += 1
while r >= 1 and a[r] == r:
    r -= 1
if l < n and a[l:r + 1] == list(range(r, l - 1, -1)):
    print(l, r)
else:
    print('0 0')
