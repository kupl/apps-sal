N, D = list(map(int, input().split()))
ds = list(map(int, input().split()))
Q = int(input())
querys = list([int(x) - 1 for x in input().split()])

# ps[i]: i回目の移動後の位置（目的地までの距離）
ps = [0] * (N + 1)
ps[0] = D
for i in range(N):
    ps[i + 1] = min(abs(ps[i] - ds[i]), ps[i])

if ps[N] != 0:
    print(('\n'.join(['YES'] * Q)))
    return

# ms[i]: i番目の移動後にm以下の位置ならば全て、目的地に到達可能であるようなmの最大値
ms = [0] * (N + 1)
for i in range(N)[::-1]:
    if ms[i + 1] + 1 >= ds[i] - ms[i + 1]:
        ms[i] = ms[i + 1] + ds[i]
    else:
        ms[i] = ms[i + 1]

for q in querys:
    if ps[q] <= ms[q + 1]:  # 妨害は不可能
        print('NO')
    else:
        print('YES')
