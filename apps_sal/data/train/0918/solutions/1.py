# cook your dish here
for i in range(int(input())):
    x=int(input())
    ans=(pow(2, x, 8589934592)-1)%8589934592
    sol = "Case "+str((i+1))+": "+str(ans)
    print(sol)
