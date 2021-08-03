n = int(input())
r = [0] * (n + 1)
a = [0] * (n + 1)
a[1:-1] = list(map(int, input().split()))
s = [(0, 0)]
for i in range(1, n + 2):
    while a[i] < s[-1][0]:
        r[i - s[-2][1] - 1] = max(s[-1][0], r[i - s[-2][1] - 1])
        del s[-1]
    s += [(a[i], i)]
for i in range(n):
    r[-i - 2] = max(r[-i - 2], r[-i - 1])
print(' '.join(map(str, r[1:])))


# Made By Mostafa_Khaled
