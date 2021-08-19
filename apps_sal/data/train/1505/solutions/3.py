n = int(input())
a = list(map(int, input().strip().split()))
i = 0
x = 0
z = 0
nest = 1
pos = 0
seq = 1
posq = 0
while i < n:
    j = i + 1
    x = 1
    z = 1
    q = i
    while j < n and x > 0:
        if a[j] == 1:
            x += 1
            z += 1
            if nest < x:
                nest = x
                pos = j
            if seq < z:
                seq = z
                posq = q
        else:
            x -= 1
        i = j + 1
        j += 1
print(nest, pos + 1, 2 * seq, posq + 1)
