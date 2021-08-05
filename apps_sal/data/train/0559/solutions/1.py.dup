import math
import copy
try:
    import psyco
    psyco.full()
except ImportError:
    pass


def isSharp(ang):
    return ang > math.pi / 4 + 0.00001


def unitVector(p2, p1):
    d0 = p2[0] - p1[0]
    d1 = p2[1] - p1[1]
    d = math.sqrt(d0 * d0 + d1 * d1)
    if d != 0:
        return [d0 / d, d1 / d]
    return [0, 0]


def compVectors(P):
    V = []
    for i in range(1, len(P)):
        v = unitVector(P[i], P[i - 1])
        if v[0] == 0 and v[1] == 0:
            return None
        V.append(v)
    return V


def angle(v2, v1):
    d = v2[0] * v1[0] + v2[1] * v1[1]
    if d > 1:
        d = 1
    if d < -1:
        d = -1
    return math.acos(d)


def compAngles(V):
    A = []
    for i in range(len(V) - 1):
        A.append(angle(V[i + 1], V[i]))
    return A


def updateAngles(i, P, V, A):
    if i - 1 >= 0:
        V[i - 1] = unitVector(P[i], P[i - 1])
    if i + 1 < len(P):
        V[i] = unitVector(P[i + 1], P[i])
    if i - 2 >= 0:
        A[i - 2] = angle(V[i - 1], V[i - 2])
    if i - 1 >= 0 and i + 1 < len(P):
        A[i - 1] = angle(V[i], V[i - 1])
    if i + 2 < len(P):
        A[i] = angle(V[i + 1], V[i])


def checkMoves(check, P, V, A, filled):
    for i in check:
        if i < 0 or i >= len(P):
            break
        x, y = P[i]
        for j in range(51):
            for k in range(51):
                P[i][0] = j
                P[i][1] = k
                if str(P[i]) in filled:
                    continue
                updateAngles(i, P, V, A)
                fixed = True
                if i - 2 >= 0:
                    if isSharp(A[i - 2]):
                        fixed = False
                if i - 1 >= 0 and i - 1 < len(A):
                    if isSharp(A[i - 1]):
                        fixed = False
                if i < len(A):
                    if isSharp(A[i]):
                        fixed = False
                if fixed:
                    return True
        P[i] = [x, y]
        updateAngles(i, P, V, A)
    return False


def canFix(first, last, P, V, A, filled):
    d = last - first
    if d > 2:
        return False
    if d == 2:
        check = [first + 2]
    if d == 1:
        check = [first + 1, first + 2]
    if d == 0:
        check = [first, first + 1, first + 2]
    if checkMoves(check, P, V, A, filled):
        return True
    return False


T = int(input())
for i in range(T):
    N = int(input())
    P = []
    V = []
    filled = {}
    for i in range(N):
        P.append(list(map(int, input().split())))
        filled[str(P[i])] = 1
    V = compVectors(P)
    A = compAngles(V)
    blunt = True
    first = -1
    last = -1
    for i in range(len(A)):
        if isSharp(A[i]):
            blunt = False
            last = i
            if first < 0:
                first = i
    if blunt:
        print('yes yes')
    else:
        if canFix(first, last, P, V, A, filled):
            print('no yes')
        else:
            print('no no')
