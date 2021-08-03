import sys

input = sys.stdin.readline

R, C, N = list(map(int, input().split()))


def is_on_edge(x, y):
    return x == 0 or x == R or y == 0 or y == C


line = []
for i in range(0, N):
    x1, y1, x2, y2 = list(map(int, input().split()))
    if is_on_edge(x1, y1) and is_on_edge(x2, y2):
        line.append([x1, y1, x2, y2])

n = len(line)
query = []
for i in range(n):
    x1, y1, x2, y2 = line[i]
    if y1 == 0:
        query.append([x1, i])
    elif x1 == R:
        query.append([R + y1, i])
    elif y1 == C:
        query.append([R + C + (R - x1), i])
    else:
        query.append([2 * R + 2 * C - y1, i])

    if y2 == 0:
        query.append([x2, i])
    elif x2 == R:
        query.append([R + y2, i])
    elif y2 == C:
        query.append([R + C + (R - x2), i])
    else:
        query.append([2 * R + 2 * C - y2, i])

query.sort(reverse=True)
que = []
dic = [0 for i in range(n)]
while query:
    t, num = query.pop()
    if dic[num] == 0:
        que.append(num)
        dic[num] = 1
    else:
        if que[-1] != num:
            print("NO")
            return
        else:
            dic[num] = 2
            que.pop()
print("YES")
