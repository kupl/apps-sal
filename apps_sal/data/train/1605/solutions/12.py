a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
s = a[1] * (a[1] - 1) // 2
s1 = a[0] + a[0] * (a[0] + 1) // 2 * a[1]
s = s * s1
s = s % 1000000007
print(s)
