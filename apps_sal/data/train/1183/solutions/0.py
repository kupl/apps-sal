for __ in range(eval(input())):
    x = eval(input())
    a = list(map(int,input().split()))
    key = eval(input())
    query = eval(input())
    maxvisited = x #maximum visted value
    j = x-1
    ans = []
    val = 0
    while j>=0:
        if a[j]==key:
            ans.append(val+1)
            val = val +1
        else: ans.append(val)
        j-=1
    ans.reverse()
    #print ans
    for ii in range(query):
        W = eval(input())
        print(ans[W], end=' ')
        print(x-W, end=' ')
        #print maxvisited, W
        if maxvisited>W:
            print(maxvisited-W+1)
            maxvisited = W
        else: print('1')

