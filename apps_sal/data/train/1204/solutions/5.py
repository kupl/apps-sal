try:
    t = int(input())
    for v in range(t):
        s = input()
        r = input()
        i = 0
        prev = -1
        top = 0
        l = 0
        k = 0
        gap = []
        while(i < len(s)):
            if(s[i] != r[i]):
                if(prev != -1):
                    gap.append(i - prev - 1)
                    top += 1
                k += 1
                while(i < len(s) and s[i] != r[i]):
                    l += 1
                    prev = i
                    i += 1
            i += 1
        gap.sort()
        ans = k * l
        for i in range(top):
            l = l + gap[i]
            k = k - 1
            if(ans > k * l):
                ans = k * l
        print(ans)
except:
    pass
