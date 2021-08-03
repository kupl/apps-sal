mod = 1000000007
dp = []
dp.append(1)
tens = []
tens.append(10)
tws = []
tws.append(1)
for i in range(1, 21):
    tens.append(tens[i - 1] * tens[i - 1])
    dp.append(dp[i - 1] * tens[i - 1] + dp[i - 1])
    tws.append(tws[i - 1] * 2)

t = eval(input())
t = int(t)
for i in range(0, t):
    now = 0
    b, a = input().split()
    a = int(a)
    b = int(b)
    j = 20
    val = 0
    while(j >= 0):
        if(b >= tws[j]):
            val *= tens[j]
            val += dp[j]
            b -= tws[j]
        j -= 1
    val *= a
    act = val * val
    now = str(act)
    # print(now)
    dow = 1
    ans = 0
    for c in now:
        x = int(c)
        # print(x)
        # print(dow)
        ans += (dow * x)
        dow *= 23
        dow %= mod
        ans %= mod
    print(ans)
    # digs=[]
    # while(act >0):
    #   d=act%10
    #   digs.append(d)
    #   act=act/10
    # now=0
    # while (act > 0):
    #   d=act%10
    #   now*=10
    #   now+=d
    #   act=act/10
    # count=0
    # ans=0
    # mul=1
    # while (now > 0):
    #   d=now%10
    #   ans+=(mul*d)
    #   ans%=mod
    #   now/=10
    #   count+=1
    #   mul*=23
    #   mul%=mod
    # print(ans)
