from sys import stdin
input = stdin.readline
n = int(input())
val = [0] * (n + 1)
add = [0] * (n + 1)
ptr = 1
sum = 0
res = [0] * n
for i in range(n):
    l = [int(x) for x in input().split()]
    if l[0] == 1:
        (a, x) = l[1:]
        add[a - 1] += x
        sum += a * x
    elif l[0] == 2:
        k = l[1]
        val[ptr] = k
        sum += k
        ptr += 1
    else:
        ptr -= 1
        sum -= val[ptr]
        sum -= add[ptr]
        add[ptr - 1] += add[ptr]
        add[ptr] = 0
    res[i] = sum / ptr
print('\n'.join((str(x) for x in res)))
