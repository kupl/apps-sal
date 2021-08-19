import sys


def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


for _ in range(II()):
    def rot(top):
        aa[top], aa[top + 1], aa[top + 2] = aa[top + 2], aa[top], aa[top + 1]

    n = II()
    aa = LI()
    bb = aa[:]
    bb.sort()
    ans = []
    for i in range(n - 2):
        j = i
        while aa[j] != bb[i]:
            j += 1
        while j > i:
            if i == j - 1:
                rot(i)
                rot(i)
                ans += [i + 1, i + 1]
                j = i
            else:
                rot(j - 2)
                ans += [j - 1]
                j -= 2
            # print(i,aa,bb,ans)

    if bb[-1] == aa[-1]:
        print(len(ans))
        print(*ans)
    else:
        for i in range(n - 3, -1, -1):
            rot(i)
            ans += [i + 1]
            if aa[i] == aa[i + 1]:
                print(len(ans))
                print(*ans)
                break
        else:
            print(-1)
