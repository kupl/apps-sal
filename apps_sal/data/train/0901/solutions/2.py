T = int(input())
for t in range(T):
    (n,k,s) = [int(x) for x in input().split()]
    input()

    ans = ""
    for i in range(1,n+1):
        ans += str(i) + " "
    print(ans)

