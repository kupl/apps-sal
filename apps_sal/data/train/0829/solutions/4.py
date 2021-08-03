n = int(input())
a = list(map(int, input().strip().split()))
a.sort()
s = 0
for i in range(len(a)):
    s += a[i] * (i - (len(a) - 1 - i))

print(s)
