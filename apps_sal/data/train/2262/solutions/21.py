def main():
    import sys
    input = sys.stdin.readline

    R, C, N = map(int, input().split())
    P = []
    X = {0, R}
    Y = {0, C}
    M = 0
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        if (x1 in X or y1 in Y) and (x2 in X or y2 in Y):
            if y1 == 0:
                L1 = x1
            elif x1 == R:
                L1 = R + y1
            elif y1 == C:
                L1 = 2 * R + C - x1
            else:
                L1 = 2 * (R + C) - y1

            if y2 == 0:
                L2 = x2
            elif x2 == R:
                L2 = R + y2
            elif y2 == C:
                L2 = 2 * R + C - x2
            else:
                L2 = 2 * (R + C) - y2

            P.append([min(L1, L2), max(L1, L2)])
    P = sorted(P, key=lambda a: a[0])
    M = len(P)

    flag = 0
    Q = []
    for i in range(M):
        x1, x2 = P[i]
        if Q == []:
            Q.append([x1, x2])
        else:
            while Q != [] and Q[-1][1] < x1:
                Q.pop()
            if Q == []:
                Q.append([x1, x2])
            else:
                y1, y2 = Q[-1]
                if y2 < x2:
                    flag = 1
                    break
                else:
                    Q.append([x1, x2])
    if flag == 1:
        print("NO")
    else:
        print("YES")


main()
