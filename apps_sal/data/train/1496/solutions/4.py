mod=1000000007
for _ in range(int(input())):
    s=input().strip()
    level=1
    ans=1
    for a in s:
        if level%2!=0:
            if a=="l":
                ans=2*ans
            else:
                ans=2*ans+2
        else:
            if a=="l":
                ans=2*ans-1
            else:
                ans=2*ans+1
        ans=ans%mod
        level+=1  


    print(ans)
