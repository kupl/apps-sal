n, m = list(map(int, input().strip().split()))
dp1, dp2, dp3, dp4 = [[[0 for i in range(m+1)] for i in range(n+1)] for i in range(4)]

# print(dp1)
# print(dp2)
# print(dp3)
# print(dp4)

a = []
for i in range(n):
    a.append(list(map(int, input().strip().split())))

for i in range(n):
    for j in range(m):
        dp1[i][j] = a[i][j] + max(dp1[i-1][j], dp1[i][j-1])

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        dp2[i][j] = a[i][j] + max(dp2[i+1][j], dp2[i][j+1])

for i in range(n-1, -1, -1):
    for j in range(m):
        dp3[i][j] = a[i][j] + max(dp3[i+1][j], dp3[i][j-1])

for i in range(n):
    for j in range(m-1, -1, -1):
        dp4[i][j] = a[i][j] + max(dp4[i-1][j], dp4[i][j+1])

# print("#############")

# for i in dp1:
#     print(i)
# print("-----------")

# for i in dp2:
#     print(i)
# print("-----------")

# for i in dp3:
#     print(i)
# print("-----------")

# for i in dp4:
#     print(i)

# print("#############")

ans = 0
for i in range(1,n-1):
    for j in range(1, m-1):
        ans = max(ans, dp1[i][j-1] + dp2[i][j+1] + dp3[i+1][j] + dp4[i-1][j], dp3[i][j-1] + dp4[i][j+1] + dp1[i-1][j] + dp2[i+1][j])
        # print(dp1[i][j-1],dp2[i][j+1], dp3[i+1][j], dp4[i-1][j], dp3[i][j-1], dp4[i][j+1], dp1[i+1][j], dp2[i-1][j])
print(ans)











