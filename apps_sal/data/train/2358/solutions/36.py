import heapq

xs, ys, xt, yt = list(map(int, input().split()))
N = int(input())
XYR = [list(map(int, input().split())) for i in range(N)]
XYR.append([xs, ys, 0])
XYR.append([xt, yt, 0])
L = [[9999999999]*(N+2) for i in range(N+2)]
for i in range(N+2):
    for j in range(i, N+2):
        x1, y1, r1 = XYR[i]
        x2, y2, r2 = XYR[j]
        L[i][j] = L[j][i] = max(((x1-x2)**2+(y1-y2)**2)**0.5-r1-r2, 0.0)


# 計算量 O((E+V)logV)
num = N+2  # グラフのノード数
start = num-2

distance = [float('inf') for i in range(num)]  # 始点から各頂点までの最短距離を格納する
prev = [float('inf') for i in range(num)]  # 最短経路における，その頂点の前の頂点のIDを格納する
distance[start] = 0
q = []  # プライオリティキュー．各要素は，(startからある頂点vまでの仮の距離, 頂点vのID)からなるタプル
heapq.heappush(q, (0, start))  # 始点をpush

while len(q) != 0:
    prov_cost, src = heapq.heappop(q)  # pop

    # プライオリティキューに格納されている最短距離が，現在計算できている最短距離より大きければ，distの更新をする必要はない
    if distance[src] < prov_cost:
        continue

    # 他の頂点の探索
    for destination, cost in enumerate(L[src]):
        if distance[destination] > distance[src] + cost:
            distance[destination] = distance[src] + cost  # distの更新
            heapq.heappush(q, (distance[destination], destination))  # キューに新たな仮の距離の情報をpush
            prev[destination] = src  # 前の頂点を記録

print((distance[-1]))

