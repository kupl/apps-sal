n = int(input())
str_a = input()
str_b = input()

a = []
b = []

for i in range(n):
    a.append(int(str_a[i]))
    b.append(int(str_b[i]))

res = 0
for i in range(n):
    if i < n - 1 and ((a[i] == 0 and a[i + 1] == 1 and b[i] == 1 and b[i + 1] == 0)or (a[i]) == 1 and a[i + 1] == 0 and b[i] == 0 and b[i + 1] == 1):
        a[i], a[i + 1] = b[i], b[i + 1]
        res+= 1
    else:
        if a[i] != b[i]:
            a[i] = b[i]
            res+= 1

print(res)
