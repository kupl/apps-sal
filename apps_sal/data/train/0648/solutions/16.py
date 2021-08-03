
from sys import stdin, stdout
n, q = list(map(int, stdin.readline().split()))
hillheight = list(map(int, stdin.readline().split()))

for i in range(q):
    t = list(map(int, stdin.readline().split()))
    if t[0] == 1:
        position = t[1] - 1
        numberofjumps = t[2]
        for k in range(position, n):
            if k - position > 100 or numberofjumps == 0:
                break
            if hillheight[k] > hillheight[position]:
                position = k
                numberofjumps = numberofjumps - 1
        stdout.write("{}\n".format(position + 1))
    elif t[0] == 2:
        L = t[1]
        R = t[2]
        X = t[3]
        for w in range(L - 1, R):

            hillheight[w] = hillheight[w] + X
