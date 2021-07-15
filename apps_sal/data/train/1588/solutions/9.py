# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    l = []
    hash = {}
    for i in range(n):
        a,b = map(str,input().split())
        l.append([a,b])
        try:
            hash[b]
        except:
            hash[b]=1
        else:
            hash[b]+=1
    ans = []
    for i in l:
        a,b = i
        if hash[b] == 1:
            ans.append([int(b),a])
    ans.sort()
    if ans!=[]:
        print(ans[0][1])
    else:
        print('Nobody wins.')







