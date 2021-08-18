try:
    t = int(input())
    while(t):
        t = t - 1
        n, k = map(int, input().split())
        q = list(map(int, input().split()))
        days, rem = 0, 0
        for i in range(n):
            rem += q[i]
            if(rem >= k):
                rem -= k
            else:
                days = i + 1
                break
            days += 1
        if(rem >= k):
            days += (rem // k) + 1
        print(days)
except:
    pass
