n = eval(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
m = eval(input())
for i in range(m):
    l, r = input().split()
    l = int(l) - 1
    r = int(r)
    s = a[l:r]
    s.sort()
    sum = 0
    for i in range(1, r - l):
        sum += (s[i] - s[i - 1])**2

    print(sum)
