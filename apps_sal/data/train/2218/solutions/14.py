import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
q = int(input())
a2 = [-1] * len(a)
arr = [None] * q
pay = [-1] * q
for i in range(q):
    b = input().split()
    if len(b) == 2:
        pay[i] = int(b[1])
    else:
        arr[i] = int(b[1])
        a2[arr[i] - 1] = int(b[2])

pay_max = max(pay)
pay_maxi = q - pay[::-1].index(pay_max) - 1
a = [pay_max if x < pay_max else x for x in a]
m = [0] * q
ma = -1
for i in range(q - 1, -1, -1):
    if pay[i] != -1:
        ma = max(ma, pay[i])
    m[i] = ma
for i in range(q):
    if arr[i]:
        if i > pay_maxi:
            a[arr[i] - 1] = max(a2[arr[i] - 1], m[i])
        else:
            a[arr[i] - 1] = max(a2[arr[i] - 1], pay_max)
print(*a)
#print(' '.join([str(x) for x in a]))
