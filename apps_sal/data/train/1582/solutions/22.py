n = int(input())
c = 0
l = str(input())
for i in range(n - 1):
    if l[i] == l[i + 1]:
        c += 1
print(c)
