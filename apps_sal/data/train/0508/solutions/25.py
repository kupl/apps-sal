import bisect
(N, Q) = map(int, input().split())
road = []
pos = []
for _ in range(N):
    (s, t, x) = map(int, input().split())
    road.append((s - x, t - x, x))
for _ in range(Q):
    pos.append(int(input()))
road.sort(key=lambda x: x[2])
ans = [-1] * Q
ischecked = [-1] * Q
for (s, t, x) in road:
    l = bisect.bisect_left(pos, s)
    r = bisect.bisect_left(pos, t)
    while l < r:
        if ischecked[l] == -1:
            ischecked[l] = r
            ans[l] = x
            l += 1
        else:
            l = ischecked[l]
for i in range(Q):
    print(ans[i])
