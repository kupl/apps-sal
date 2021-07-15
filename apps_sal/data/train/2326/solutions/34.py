N = int(input())
A = [0] + list(map(int, input().split()))

# 実体Bと大きい順にループを回してindexを取得するためだけのC
B = [[a, i, 1] for i, a in enumerate(A)]
C = sorted(B, reverse=True)

# 自分より左側で最大となる値と位置
# 最大となる値が複数ある場合は最も左のものを採用
a_max, idx = 0, 0 # [value, idx]
left_max = [[0, 0] for i in range(N+1)] # [value, idx]
for i, a in enumerate(A):
  left_max[i] = [a_max, idx]
  if a > a_max:
    a_max, idx = a, i

ans = [0] * (N+1)
next_i = C[0][1]
for _, i, _ in C: # indexだけ取得
  a, _, num = B[i] # 実体を取得、numは右側で同じ数になったとき、同じ山と見なして計算量削減
  if i == next_i:
    next_a, next_i = left_max[i] # 次の最大値であるnext_aになるまではこのiがsに追加される
    now_i = i
    ans[i] += (a - next_a) * num # 差分(a-next_a)をnum回分追加
    B[next_i][2] += num # 残った分はnext_iの石が消されるタイミングで消されるのでまとめる
  else:
    ans[now_i] += (a - next_a) * num
    B[next_i][2] += num

print(*ans[1:], sep='\n')
