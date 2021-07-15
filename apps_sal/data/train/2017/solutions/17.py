j = int(input()) * 2
l = list(map(int, input().split()))
for i in range(0, j, 2):
    if l[i] != l[i + 1]:
        break
for j in range(j, 1, -2):
    if l[j - 2] != l[j - 1]:
        break
l, res = l[i:j], 0
while l:
    i = l.index(l.pop())
    res += len(l) - i - 1
    del l[i]
print(res)
