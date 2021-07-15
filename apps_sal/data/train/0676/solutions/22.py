# cook your dish here

tests = int(input())
for te in range(tests):
    n = int(input())
    strings = list(input().split())
    #print(strings)
    dic = {}
    for i in range(n):
        if(strings[i] not in dic):
            dic[strings[i]] = 1
        else:
            dic[strings[i]] += 1
    maxa = -1
    for i in list(dic.keys()):
        if(dic[i]>maxa):
            ans = i
            maxa = dic[i]
        if(dic[i] == maxa):
            ans = min(ans,i)

    print(ans)
    

