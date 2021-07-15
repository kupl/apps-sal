def main():
    s=input()
    n=len(s)
    if s[n-1]=="1" or s[0]=="0":
        print(-1)
        return 0
    for i in range(n//2):
        if s[i]!=s[n-i-2]:
            print(-1)
            return 0
    t=[]
    now=1
    for i in range(n//2-1):
        t.append([now,i+2])
        if s[i]=="1":
            now=i+2
    t2=[[i+n//2,j+n//2] for i,j in t]
    if s[n//2-1]=="1":
        t.append([now,now+n//2])
    else:
        for i in range(len(t2)):
            if t2[i][0]==now+n//2:
                t2[i][0]=now
            if t2[i][1]==now+n//2:
                t2[i][1]=now
        t.append([now,now+n//2])
    if n%2==1:
        t.append([now,n])
    t+=t2
    for i,j in t:
        print(i,j)
main()
