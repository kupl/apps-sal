def int_list():
    return [int(c) for c in input().split()]


def int1():
    return int(input())


def str_list():
    return [c for c in input().split()]


def str1():
    return input()


s1 = ("RGB" * 66667)[:-1]
s2 = ("GBR" * 66667)[:-1]
s3 = ("BRG" * 66667)[:-1]

q = int1()
res = []

for j in range(q):
    n, k = int_list()
    s = str1()

    c1 = []
    c2 = []
    c3 = []

    for i in range(n):
        if s[i] != s1[i]:
            c1.append(1)
        else:
            c1.append(0)
        if s[i] != s2[i]:
            c2.append(1)
        else:
            c2.append(0)
        if s[i] != s3[i]:
            c3.append(1)
        else:
            c3.append(0)

    min1 = sum(c1[:k])
    min2 = sum(c2[:k])
    min3 = sum(c3[:k])

    cost1 = min1
    cost2 = min2
    cost3 = min3

    for i in range(k, n):
        cost1 += (c1[i] - c1[i - k])
        cost2 += (c2[i] - c2[i - k])
        cost3 += (c3[i] - c3[i - k])

        min1 = cost1 if cost1 < min1 else min1
        min2 = cost2 if cost2 < min2 else min2
        min3 = cost3 if cost3 < min3 else min3

    res.append(min(min1, min2, min3))

for result in res:
    print(result)
