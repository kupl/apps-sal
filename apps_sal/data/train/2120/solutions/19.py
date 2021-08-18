from sys import stdin
input = stdin.readline
n, sum, point = int(input()), 0, 1
num = (n + 1) * [0]
f = (n + 1) * [0]
for i in range(n):
    k = list(map(int, input().split()))
    if k[0] == 1:
        f[k[1] - 1] += k[2]
        sum += k[2] * k[1]
    elif k[0] == 2:
        num[point] = k[1]
        sum += k[1]
        point += 1
    elif k[0] == 3:
        point -= 1
        sum -= num[point] + f[point]
        f[point - 1] += f[point]
        f[point] = 0
    print('%.6f' % (sum / point))
