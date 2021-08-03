n = int(input())
a = input()
e = a[0]
f = 0
for i in range(1, n):
    if a[i] == e:
        f += 1
    else:
        e = a[i]
print(f)
