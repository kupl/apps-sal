s = input().strip()
d = {}
k = 27
sum = 0
for i in range(65, 91):
    d[chr(i)] = k
    k = k - 1
for i in s:
    sum = sum + d[i]
print(sum)
