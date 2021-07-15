n = int(input())
a = input()
b = input()

ao = a.count('1')
az = n - ao

u, v = 0, 0

for i in range(n):
    if b[i] == '0':
        if a[i] == '1':
            u += 1
        else:
            v += 1

print(u * az + v * ao - u * v)

