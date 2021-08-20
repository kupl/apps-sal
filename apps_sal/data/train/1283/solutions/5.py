import sys
n = 201
v = [0 for i in range(n + 1)]


def gen():
    for i in range(1, n + 1):
        v[i] = i
    countDivision = [0 for i in range(n + 1)]
    for i in range(n + 1):
        countDivision[i] = 2
    for i in range(2, n + 1, 1):
        if v[i] == i and countDivision[i] == 2:
            for j in range(2 * i, n + 1, i):
                if countDivision[j] > 0:
                    v[j] = int(v[j] / i)
                    countDivision[j] -= 1


try:
    t = int(sys.stdin.readline())
    for _ in range(t):
        gen()
        x = int(sys.stdin.readline())
        flag = 0
        for i in range(2, x // 2 + 1):
            if v[i] == 1 and v[x - i] == 1:
                flag = 1
        if flag == 1:
            print('YES')
        else:
            print('NO')
except:
    pass
