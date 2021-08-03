N = int(input())
Ball = []
for i in range(N):
    x, y = list(map(int, input().split()))
    x, y = min(x, y), max(x, y)
    Ball.append((x, y))

Ball.sort()  # ソートしておく
X = [x for x, y in Ball]
Y = [y for x, y in Ball]

# 全体のMIN, MAX
MIN = X[0]
MAX = max(Y)

# 確定2玉を別グループに
ans = (max(X) - MIN) * (MAX - min(Y))

# 確定2玉を同じグループに

# 全体のMAX・MINが確定している場所は、もう片方を使うしかない
MIN_index, MAX_index = X.index(MIN), Y.index(MAX)

# 選ばざるを得ないやつ
MIN_O = X[MAX_index]
MAX_O = Y[MIN_index]
MIN_O, MAX_O = min(MIN_O, MAX_O), max(MIN_O, MAX_O)

# 選択肢がないやつを削除
Ball = [Ball[i] for i in range(N) if i not in (MIN_index, MAX_index)]

# つくりおし
X = [x for x, y in Ball]
Y = [y for x, y in Ball]

# とりあえず小さいほうを集めたことにしておく
B = [x for x in X] + [MAX_O, MIN_O]
B_max = max(B)

for i in range(len(Ball)):
    x, y = X[i], Y[i]
    if B_max - x > B_max - y >= 0:
        B[i] = y
    else:
        break

ans = min(ans, (MAX - MIN) * (max(B) - min(B)))
print(ans)
