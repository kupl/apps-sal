# cook your dish here
n, m, w, b, *l = list(map(int, input().split()))
mat = [[0 for _ in range(m)] for _ in range(n)]
for i in range(w):
    y, x = l[2 * i], l[2 * i + 1]
    mat[y - 1][x - 1] = 1

for i in range(w, w + b):
    y, x = l[2 * i], l[2 * i + 1]
    mat[y - 1][x - 1] = 2

temp = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
for j in range(n):
    prev_w = -1
    blk = m - 1
    for i in range(m - 1, -1, -1):
        if mat[j][i] == 2:
            blk = i
            prev_w = -1
        elif mat[j][i] == 1:
            if prev_w != -1:
                blk = prev_w
            prev_w = i
        else:
            ans += blk - i + 1
            temp[j][i] = blk - i + 1
print(ans)
# print(temp)
