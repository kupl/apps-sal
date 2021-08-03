import sys
n, x, y = input().split(' ')
n = int(n)
x = int(x)
y = int(y)
contests = {}

for i in range(n):
    s, e = input().split(' ')
    s = int(s)
    e = int(e)
    contests[(s, e)] = abs(s - e)

v_time = input().split(' ')
w_time = input().split(' ')

v_time, w_time = list(map(int, v_time)), list(map(int, w_time))
v_time.sort()
w_time.sort()


score = sys.maxsize

contests = dict(sorted(contests.items(), key=lambda item: item[1]))
for k, v in contests.items():
    start = -1
    end = sys.maxsize
    for i in range(x):
        if v_time[i] > k[0]:
            break
        start = v_time[i]
    for j in range(y):
        if w_time[j] >= k[1]:
            end = w_time[j]
            break
    if start == -1:
        continue
    score = min(score, (end - start + 1))
    if score - 1 <= v:
        break

print(score)
