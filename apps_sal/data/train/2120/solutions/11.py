import sys


d, ans = [0], []
s = 0

for _ in range(int(next(sys.stdin))):
    cmd = tuple(map(int, next(sys.stdin).split()))
    if cmd[0] == 1:
        s += cmd[1] * cmd[2]
        if cmd[1] == len(d):
            d[-1] += cmd[2]
        else:
            d[cmd[1] - 1] -= cmd[2]
    elif cmd[0] == 2:
        s += cmd[1]
        d.append(cmd[1])
        d[-2] = d[-1] - d[-2]
    else:
        s -= d[-1]
        d[-2] = d[-1] - d[-2]
        d.pop()

    # print(cmd, len(d), '-->', d)
    ans.append(str(s / len(d)))

print('\n'.join(ans))

