n = int(input())
a = input()
b = input()
zer = 0
one = 0
ta = a.count('1')
tz = a.count('0')
for i in range(n):
    if a[i] == '0' and b[i] == '0':
        zer += 1
    elif a[i] == '1' and b[i] == '0':
        one += 1
ans = zer * ta + one * tz - zer * one
print(ans)
