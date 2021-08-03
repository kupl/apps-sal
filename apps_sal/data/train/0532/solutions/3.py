
# // Problem : Zero One Tiles
# // Contest : CodeChef - IARCS OPC Judge Problems
# // URL : https://www.codechef.com/IARCSJUD/problems/TILES01
# // Memory Limit : 256 MB
# // Time Limit : 1000 ms
# // Powered by CP Editor (https://github.com/cpeditor/cpeditor)

dp = [None] * 1000010
dp[0] = 0
dp[1] = 1
MOD = 15746
n = int(input())
for i in range(2, n + 2):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
print(dp[n + 1])
