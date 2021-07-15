n, k = map(int, input().split())
a = [0] * n
b = ['0'] * n
c = []
s = input()
for i in range(n):
    if k != 0:
        if s[i] == '(':
            c.append(i)
        else:
            d = c.pop()
            a[i] = 1
            a[d] = 1
            k -= 2
for i in range(n):
    if a[i] == 1:
        print(s[i], end = '')

