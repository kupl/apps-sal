from math import sqrt
r = int(input())
cnt = 0
rt = []
for i in range(1, 10 * r):
    for j in range(i, 150):
        for k in range(j + 1, j + i):
            s = float((i + j + k)) / 2
            area = sqrt(abs(s * (s - i) * (s - j) * (s - k)))
            if (r == (float(2 * area)) / (i + j + k)):
                cnt += 1
                rt.append([i, j, k])

print(cnt)

for i in rt:
    for j in i:
        print(j, end=' ')
    print()
