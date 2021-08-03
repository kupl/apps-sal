import sys
input = sys.stdin.readline

A = input().rstrip()
dp = [chr(c) for c in range(ord('a'), ord('z') + 1)]
for c in A[::-1]:
    s = min(dp, key=lambda x: len(x))
    dp[ord(c) - ord('a')] = c + s
print(min(dp, key=lambda x: len(x)))
