for t in range(int(input())):
    pts=list(input())
    ans=0
    if pts[0]=='0':
        ans=0
    else:
        for i in range(1,len(pts),1):
            if pts[i]=='0':
                ans=ans+1
            if pts[i-1]=='0':
                if pts[i]=='1':
                    break
    print(ans)

