from collections import deque


def comb(m):
    if m < 3:
        return 0
    else:
        return int(m * (m - 1) * (m - 2) / 6)


n, d = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
cnt = 0
de = deque()
temp = 0
for i in range(n):
    if i == 0:
        de.append(x[i])
    else:
        if de[0] + d < x[i]:
            cnt += comb(len(de)) - comb(temp)
            while len(de) != 0 and de[0] + d < x[i]:
                de.popleft()
            temp = len(de)
        de.append(x[i])
    # print(de)
cnt += comb(len(de)) - comb(temp)
print(cnt)
