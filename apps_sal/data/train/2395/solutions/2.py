import sys
def input(): return sys.stdin.readline().rstrip()


def calc(S):
    f = 0
    A = []
    B = []
    for s in S:
        a = int(s)
        if a == 1:
            if f:
                A.append("0")
                B.append("1")
            else:
                f = 1
                A.append("1")
                B.append("0")
        if a == 0:
            A.append("0")
            B.append("0")
        if a == 2:
            if f:
                A.append("0")
                B.append("2")
            else:
                A.append("1")
                B.append("1")
    print("".join(A))
    print("".join(B))


T = int(input())
for _ in range(T):
    N = int(input())
    calc(input())
