# cook your dish here
(n, m, k) = list(map(int, input().split()))
lec = []
que = []
for i in range(n):
    l = list(map(int, input().split()))
    que.append(l[-1])
    lec.append(sum(l) - l[-1])
stu = 0
for i in range(n):
    if lec[i] >= m and que[i] <= 10:
        stu += 1
    i += 1
print(stu)
