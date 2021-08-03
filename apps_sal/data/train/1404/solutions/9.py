__author__ = 'Deepak'
t = eval(input())
while t > 0:
    t -= 1
    r, g, b = list(map(int, input().split()))
    k = eval(input())
    a = [r, g, b]
    a.sort()
    if k <= a[0]:
        print(k * 3 - 2)
    elif k > a[0] and k <= a[1]:
        print(a[0] * 3 + (k - a[0]) * 2 - 1)
    else:
        print(a[0] * 3 + (a[1] - a[0]) * 2 + k - a[1])
