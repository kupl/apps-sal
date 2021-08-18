import collections
import string


def listprint(l):
    if len(l) == 0:
        print("[]")
        return
    s = "[ " + "{0:<2}".format(l[0])
    for i in range(1, len(l)):
        s += ", " + "{0:>2}".format(l[i])
    s += " ]"
    print(s)


def main():
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)
    d = collections.defaultdict(list)
    f = collections.defaultdict(list)

    for i in range(n - 1, -1, -1):
        d[b[i]].append(i)

    tmp = []
    for i in range(n):

        whereInB = d[a[i]][-1]

        if a[i] in f:
            z = 1 + f[a[i]][-1]
            if whereInB != 0 and (b[whereInB - 1] in f):
                prevNumberList = f[b[whereInB - 1]]
                p = prevNumberList
                if len(p) == len(d[b[whereInB - 1]]):
                    z = max(z, p[0] + len(p))
                else:
                    z = max(z, 1 + len(p))
            f[a[i]].append(z)
            tmp.append(f[a[i]][-1])
            continue

        if whereInB == 0 or (b[whereInB - 1] not in f):
            f[a[i]].append(1)
        else:
            if len(d[b[whereInB - 1]]) == len(f[b[whereInB - 1]]):
                prevNumberList = f[b[whereInB - 1]]
                p = prevNumberList
                f[a[i]].append(p[0] + len(p))
            else:
                f[a[i]].append(1 + len(f[b[whereInB - 1]]))

        tmp.append(f[a[i]][-1])

    print(n - max(map(max, f.values())))


tn = int(input())
for _ in range(tn):
    main()
