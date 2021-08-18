t = int(input())
while(t > 0):
    n = int(input())
    s = input().split(" ")
    dic = {}
    for i in range(len(s[0])):
        for j in range(i, len(s[0])):
            dic[s[0][i:j + 1]] = 1
    for i in range(1, len(s)):
        for j in range(len(s[i])):
            for k in range(j, len(s[i])):
                x = dic.get(s[i][j:k + 1], -1)
                if(x == i):
                    dic[s[i][j:k + 1]] += 1
    ans = ""
    for x in dic:
        if(dic[x] == n):
            if(len(x) >= len(ans)):
                ans = x
    for x in dic:
        if(len(x) == len(ans) and dic[ans] == dic[x]):
            ans = min(ans, x)
    print(ans)
    t -= 1
