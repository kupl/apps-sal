def dot(a, b, c):
    return a + c*b

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    dp = [ 0 for _ in range(n) ]
    st = [0 for _ in range(n) ]
    i, j = 0,  0

    for k in range(1,n):
        while(j - i > 0 and dot(dp[st[i]],b[st[i]],a[k]) >= dot(dp[st[i+1]],b[st[i+1]],a[k])):
            i+=1
        dp[k] = a[k]*b[st[i]] + dp[st[i]]
        while(j - i > 0 and (b[st[j]] - b[k])*(dp[st[j]] - dp[st[j-1]]) > (dp[k] - dp[st[j]])*(b[st[j-1]] - b[st[j]])):
            j-=1
        j+=1
        st[j] = k


    print(dp[-1])

def __starting_point():
    main()
__starting_point()
