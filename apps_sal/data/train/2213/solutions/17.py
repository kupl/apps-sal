for t in range(int(input())):
    a,b,n = list(map(int,input().split()))
    c = a^b
    ans = [a,b,c]
    print(ans[n%3])
