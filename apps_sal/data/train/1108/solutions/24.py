# cook your dish here
n, m, k = map(int, input().split())
T = []

for i in range(n):
    temp = list(map(int, input().split()))
    T.append(temp)

ans = 0
for i in range(n):
    watchTime = 0
    Ques = T[i][k]
    for j in range(k):
        watchTime += T[i][j]
    if(watchTime >= m and Ques <= 10):
        ans += 1

print(ans)
