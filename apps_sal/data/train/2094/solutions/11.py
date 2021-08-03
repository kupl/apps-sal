n = int(input())
u = list(input())
r0 = 0
n1 = 0
for i in range(n):
    if u[i] == 'r':
        r0 += 1
    elif u[i] == 'n':
        n1 += 1
for i in range(n1):
    print(1, end=' ')
for i in range(r0):
    print(0, end=' ')
