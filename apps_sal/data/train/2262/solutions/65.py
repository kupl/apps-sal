w, h, n = list(map(int, input().split()))

pos = []
for i in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    if (x1 in [0, w] or y1 in [0, h]) and (x2 in [0, w] or y2 in [0, h]):
        pos.append((x1, y1, i))
        pos.append((x2, y2, i))

pos.sort(key=lambda v: v[0]) # top →
edge = [v[-1] for v in pos if v[1] == 0 and v[0] != 0]

pos.sort(key=lambda v: v[1]) # left ↓
edge += [v[-1] for v in pos if v[0] == w and v[1] != 0]

pos.sort(key=lambda v: v[0], reverse=True) # bottom ←
edge += [v[-1] for v in pos if v[1] == h and v[0] != w]

pos.sort(key=lambda v: v[1], reverse=True) # right ↑
edge += [v[-1] for v in pos if v[0] == 0 and v[1] != h]

# for i in range(len(edge) - 1):
#     if edge[i] == edge[i + 1]:
#         break
# for j in range(len(edge) // 2):
#     if edge[(i + j + 1) % n] != edge[(i - j + n) % n]:
#         print("NO")
#         break
# else:
#     print("YES")

# print(edge)
hist = [None] * n
step = 0
for v in edge:
    if hist[v] is None:
        hist[v] = step + 1
        step += 1
    else:
        if hist[v] != step:
            print("NO")
            break
        step -= 1
else:
    print("YES")


