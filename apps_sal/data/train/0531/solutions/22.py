n = int(input())

occupy = [float("-inf")]
height = [0]
pos = [float("-inf")]

for i in range(n):
    p, h = list(map(int, input().split()))
    pos.append(p)
    height.append(h)
    occupy.append(p)

pos.append(float("inf"))
height.append(0)
occupy.append(float("inf"))

sol = 0
for i in range(1, n + 1):
    if pos[i] - height[i] > occupy[i - 1]:
        sol += 1
    elif pos[i] + height[i] < occupy[i + 1]:
        sol += 1
        occupy[i] = pos[i] + height[i]

print(sol)
