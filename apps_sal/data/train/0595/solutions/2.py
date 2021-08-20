st = str(input())


def checkpal(i, j, k, l):
    a = i
    b = l
    while a < b:
        if st[a] != st[b]:
            return -1
        if a == j:
            a = k - 1
        if b == k:
            b = j + 1
        a += 1
        b -= 1
    return 1


l = len(st)
count = 0
for i in range(l):
    for j in range(i, l):
        for k in range(j + 1, l):
            for m in range(k, l):
                if checkpal(i, j, k, m) == 1:
                    count += 1
print(count)
