import copy
import sys
input = sys.stdin.readline


def dfs(x, S):
    for i in range(len(S)):
        if x in S[i]:
            S[i].remove(x)
    LEN1 = 0
    for s in S:
        if len(s) == 1:
            LEN1 += 1
            ne = list(s)[0]
        if LEN1 == 2:
            return [-1]
    if LEN1 == 1:
        return [ne] + dfs(ne, S)
    else:
        return [-1]


t = int(input())
for tests in range(t):
    n = int(input())
    A = tuple((set(list(map(int, input().split()))[1:]) for i in range(n - 1)))
    for i in range(1, n + 1):
        ANS = [i] + dfs(i, copy.deepcopy(A))
        if -1 in ANS[:n]:
            continue
        else:
            USE = [0] * (n - 1)
            flag = 1
            for i in range(n - 1, 0, -1):
                SET = set()
                for j in range(i, -1, -1):
                    SET.add(ANS[j])
                    if SET in A:
                        break
                else:
                    flag = 0
                    break
            if flag:
                print(*ANS[:n])
                break
