import bisect
from collections import defaultdict
import sys
input = sys.stdin.readline

INF = 10 ** 12

N, a, b = map(int, input().split())
X_to_Y = defaultdict(lambda: [-INF, INF])
Y_to_X = defaultdict(lambda: [-INF, INF])
for i in range(1, N + 1):
    x, y = map(int, input().split())
    x, y = x + y, x - y
    X_to_Y[x].append(y)
    Y_to_X[y].append(x)
    if i == a:
        sx, sy = x, y
    elif i == b:
        tx, ty = x, y

R = max(abs(sx - tx), abs(sy - ty))

for key, arr in X_to_Y.items():
    arr.sort()
    L = len(arr)
    move_right = list(range(1, L)) + [None]
    X_to_Y[key] = [arr, move_right]

for key, arr in Y_to_X.items():
    arr.sort()
    L = len(arr)
    move_right = list(range(1, L)) + [None]
    Y_to_X[key] = [arr, move_right]

equiv_class = set([(sx, sy), (tx, ty)])

answer = 0
task = [(sx, sy), (tx, ty)]

while task:
    x, y = task.pop()
    # 既出の元も含めて辺の個数を数える
    # 未出の元を同値に追加
    # x,y両方満たすものは、x側にだけ入れる
    for x1 in [x - R, x + R]:
        if not (x1 in X_to_Y):
            continue
        arr, move_right = X_to_Y[x1]
        left = bisect.bisect_left(arr, y - R)
        right = bisect.bisect_right(arr, y + R)
        # [left, right) が辺で結べるターゲット
        answer += right - left  # 辺の個数
        i = left
        while i < right:
            y1 = arr[i]
            if (x1, y1) not in equiv_class:
                equiv_class.add((x1, y1))
                task.append((x1, y1))
            # なるべく、既に居ない元は見ないで済ませるように
            next_i = move_right[i]
            if next_i >= right:
                break
            move_right[i] = right
            i = next_i
    for y1 in [y - R, y + R]:
        if not y1 in Y_to_X:
            continue
        arr, move_right = Y_to_X[y1]
        left = bisect.bisect_left(arr, x - R + 1)
        right = bisect.bisect_right(arr, x + R - 1)
        # [left, right) が辺で結べるターゲット
        answer += right - left  # 辺の個数
        i = left
        while i < right:
            x1 = arr[i]
            if (x1, y1) not in equiv_class:
                equiv_class.add((x1, y1))
                task.append((x1, y1))
            # なるべく、既に居ない元は見ないで済ませるように
            next_i = move_right[i]
            if next_i >= right:
                break
            move_right[i] = right
            i = next_i

answer //= 2  # 両方向から辺を見た
print(answer)
