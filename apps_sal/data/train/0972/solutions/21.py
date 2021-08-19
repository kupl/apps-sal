(x, k) = map(int, input().split())
l = []
for i in range(x):
    l = l + [int(input())]
l.sort()
i = 0
min = 2 ** 64
while i + k < len(l):
    if l[i + k - 1] - l[i] < min:
        min = l[i + k - 1] - l[i]
    i += 1
print(min)
