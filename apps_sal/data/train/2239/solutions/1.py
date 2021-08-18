

import sys

sys.setrecursionlimit(20000)


def go(v, w, last):

    if game[v][w][last] >= 0:
        return(game[v][w][last])

    flag = 0

    move = 0

    for p in edges_out[v]:

        if p[1] >= last:

            move = 1

            if not go(w, p[0], p[1]):

                flag = 1

                break

    if not move or not flag:

        game[v][w][last] = 0

        return(0)

    else:

        game[v][w][last] = 1

        return(1)


n, m = [int(i) for i in input().split()]

edges_in = []

edges_out = []

for i in range(n):

    edges_in.append([])

    edges_out.append([])


for i in range(m):

    s1, s2, s3 = input().split()

    v = int(s1) - 1

    w = int(s2) - 1

    weight = ord(s3[0]) - ord('a') + 1

    edges_out[v].append((w, weight))

    edges_in[w].append((v, weight))


game = []

for i in range(n):

    tmp1 = []

    for j in range(n):

        tmp2 = []

        for c in range(27):

            tmp2.append(-1)

        tmp1.append(tmp2)

    game.append(tmp1)


for v in range(n):

    s = ''

    for w in range(n):

        if go(v, w, 0):
            s = s + 'A'

        else:
            s = s + 'B'

    print(s)
