3

n = int(input())
send = [[], []]
for _ in range(n):
    t, x, y = tuple(map(int, input().split()))
    send[t - 1].append(x)
for _ in range(2):
    print('LIVE' if 2 * sum(send[_]) >= 10 * len(send[_]) else 'DEAD')
