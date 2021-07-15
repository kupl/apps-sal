# cook your dish here
import math
N = 1000003
dp = [0] * (N + 1)
def seive():
    array = [0] * (N + 1)
    array[0] = 1
    array[1] = 1
    for i in range(2, math.ceil(math.sqrt(N) + 1)):
        if array[i] == 0:
            for j in range(i * i, N + 1, i):
                array[j] = 1
    runningPrimeSum = 0
    for i in range(1, N + 1):
        if array[i] == 0:
            runningPrimeSum += i
        dp[i] = runningPrimeSum
seive()
t=int(input())
for _ in range(t):
    n=int(input())
    print(dp[n]%10)
