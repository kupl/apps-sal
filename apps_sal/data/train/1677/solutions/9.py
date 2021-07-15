N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_prefix = [B[0]]
for i in range(1, N):
    B_prefix.append(B_prefix[-1] + B[i])
mxs = []

# for i == j
mxs.append(max(A))

# for i < j
mxI = A[0] - B_prefix[0]
total_mx = mxI + A[1] + B_prefix[0]
for i in range(1, N):
    mxI = max(mxI, A[i - 1] - B_prefix[i - 1])
    total_mx = max(total_mx, mxI + A[i] + B_prefix[i - 1])
mxs.append(total_mx)

# for i > j
mxJ = A[0]
second_mx = mxJ + A[1] - B_prefix[1]
for i in range(1, N - 1):
    # print(second_mx, mxJ)
    mxJ = max(mxJ, A[i] + B_prefix[i - 1])
    second_mx = max(second_mx, mxJ + A[i + 1] - B_prefix[i + 1])

mxs.append(second_mx + B_prefix[-1])
#
# print(*B_prefix)
print(max(mxs))


