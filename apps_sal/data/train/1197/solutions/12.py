from array import *


def main():
    t = int(input())
    if 1 <= t <= 700:
        s = array("i", [])
        ql = array("i", [])
        for x in range(t):
            ql.append(int(input()))
        n = max(ql)
        if 1 <= n <= 700:
            l = array("i", [1])
            i = 2
            a = c = set()
            b = {2}
            while len(l) < n:
                if i - 1 in l:
                    c = c.union(a.union(b))
                d = set()
                for j in l:
                    d = d.union({i + j})
                if len(c.intersection({2 * i}.union(d))) == 0:
                    b = d
                    a = {2 * i}
                    l.append(i)
                i = i + 1
            prev = 0
            for j in l:
                s.append(prev + j)
                prev = prev + j
            for j in ql:
                for i in range(j):
                    print(l[i], end=" ")
                print()
                print(s[j - 1])


main()
