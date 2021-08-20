import sys
ioRead = sys.stdin.readline


def ioWrite(x):
    return sys.stdout.write(f'{x}\n')


n = int(ioRead())
points = sorted(map(int, ioRead().split(' ')))
answer = points[-1] ** 2
for c in range(n):
    axis_1 = [points[c], points[c + n - 1]]
    axis_2 = [points[n if c == 0 else 0], points[-1]]
    c_answer = (axis_1[1] - axis_1[0]) * (axis_2[1] - axis_2[0])
    answer = min(answer, c_answer)
ioWrite(answer)
