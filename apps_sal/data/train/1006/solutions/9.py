t = int(input())
for _ in range(t):
    n, d = input().split(" ")
    q = int(d)
    k = []
    for i in n:
        k.append(i)

    k2 = k[::]

    min = int(d)
    for j in range(len(k2) - 1, -1, -1):
        if int(k2[j]) > min:
            k2.pop(j)
        else:
            min = int(k2[j])

    print(*k2, sep="", end="")
    print(d * (len(k) - len(k2)))
