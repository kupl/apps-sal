# creating a modulus function for efficiency purpose
def modulus(n):
    # defining modulus
    mod = int(1e9) + 7
    if n < 0:
        n += mod
    else:
        n = n % mod
    return n


# taking input
n, k = list(map(int, input().strip().split()))
array = list(map(int, input().strip().split()))
# creating a frequency array called freak
freak = []
for i in list(set(array)):
    freak.append(array.count(i))
# creating a DP Matrix of zeros initially
dp = [[0] * len(freak) for _ in range(k)]
# elements of first row of DP matrix will be same as the freak array
for i in range(len(freak)):
    dp[0][i] = freak[i]
# starting calculations from the second row onwards
for row in range(1, k):
    for col in range(0, len(freak) - row):
        dp[row][col] = modulus(freak[col] * sum(dp[row - 1][col + 1:]))
# answer will be sum[dp] plus 1 for empty set
ans = 1
for i in dp:
    ans += sum(i)
ans = modulus(ans)
# printing the answer
print(ans)
