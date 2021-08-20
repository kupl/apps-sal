n = int(input())
a = input()
b = input()
c = False
f = 0
l = '12'
for i in range(n):
    if a[i] != b[i]:
        if c:
            if l != a[i]:
                c = False
                f += 1
            else:
                f += 1
        else:
            c = True
    else:
        if c:
            f += 1
        c = False
    l = a[i]
if c:
    f += 1
print(f)
