# cook your dish here
t = int(input())
while(t):
    n = int(input())
    # n,k=map(int,input().split())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(len(l)):
        # print(ans^l[i])
        ans = (ans ^ l[i])

    print(ans)
    t -= 1
