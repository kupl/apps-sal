import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


def rotate(a, i):
    t = a[i + 2]
    a[i + 2] = a[i + 1]
    a[i + 1] = a[i]
    a[i] = t


def solve(n, a):
    sa = sorted(a)
    s = []

    rolled = False
    i = 0
    while i < n:
        for j in range(i, n):
            if a[j] == sa[i]:
                break
        while j - i >= 2:
            j -= 2
            rotate(a, j)
            s.append(j + 1)
        if i + 1 == j:
            if i + 2 < n:
                rotate(a, i)
                rotate(a, i)
                s.append(i + 1)
                s.append(i + 1)
            else:
                if rolled:
                    wi(-1)
                    return

                found = False
                for k in range(n - 2, 0, -1):
                    if len(set(a[k - 1:k + 2])) == 2:
                        found = True
                        break
                if found:
                    if a[k - 1] == a[k]:
                        rotate(a, k - 1)
                        rotate(a, k - 1)
                        s.append(k)
                        s.append(k)
                    else:
                        rotate(a, k - 1)
                        s.append(k)
                    rolled = True
                    i = k - 2
                else:
                    wi(-1)
                    return

        i += 1

    if len(s) <= n * n:
        wi(len(s))
        wia(s)
    else:
        wi(-1)


def main():
    for _ in range(ri()):
        n = ri()
        a = ria()
        solve(n, a)


def __starting_point():
    main()


__starting_point()
