import sys

T = int(sys.stdin.readline())
for tc in range(T):
    N, Z1, Z2 = [int(c) for c in sys.stdin.readline().strip().split()]
    A = [int(c) for c in sys.stdin.readline().strip().split()]
    A.extend([-a for a in A])

    def sol(A, Z1, Z2):
        if Z1 in A or Z2 in A:
            return 1
        else:
            if all((Z1 - s in A or Z2 - s in A) for s in A):
                return 2
        return 0
    print(sol(A, Z1, Z2))
