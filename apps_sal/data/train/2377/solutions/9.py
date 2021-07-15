tt = int(input())

for loop in range(tt):

    n = int(input())

    a = list(map(int,input().split()))
    ai = []
    for i in range(n):
        ai.append( ( a[i] , i ) )

    ai.sort()
    ind = 0

    b = [0] * n #newlist
    non = [0] * (n+1) #numbers of numbers

    for i in range(n):

        if i != 0 and ai[i][0] != ai[i-1][0]:
            ind += 1

        b[ai[i][1]] = ind
        non[ind] += 1

    dp = [0] * (n+1)

    for i in range(n):

        dp[b[i]] += max( dp[b[i]] , dp[b[i]-1] + 1)

    print (n - max(dp))
