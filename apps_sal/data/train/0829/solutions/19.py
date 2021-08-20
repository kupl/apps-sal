N = int(input())
l = list(map(int, input().strip().split(' ')))
s = 0
for i in range(N):
    for j in range(i + 1, N):
        s += abs(l[j] - l[i])
print(s)
'\nl.sort()\n\ns = 0\nfor i in range(len(l)):\n    s -= (len(l) - i - 1) * l[i]\n    s += i * l[i]\nprint(s)\n'
