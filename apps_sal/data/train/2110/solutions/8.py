l = [0] * 1100001
input()
for i in map(int, input().split()):
    l[i] += 1
for i in range(1100000):
    (l[i], l[i + 1]) = (l[i] % 2, l[i + 1] + l[i] // 2)
print(sum(l))
