# cook your dish here
def tourneyscore(a):
    scorelist=[]
    for i in range(len(a)):
        scorelist.append(0)
    for i in range(len(a)):
        for k in range(i+1,len(a)):
            x=scorelist[i]
            y=scorelist[k]
            if a[i][0]<a[k][0]and a[i][1]>a[k][1]:
                scorelist[i]=x+2
            elif a[i][0]>a[k][0]and a[i][1]<a[k][1]:
                scorelist[k]=y+2
            else:
                scorelist[i]=x+1
                scorelist[k]=y+1
    print(*scorelist, sep = " ") 

for T in range(int(input())):
    singerlist=[]
    for N in range(int(input())):
        L,U=input().split()
        L,U=int(L),int(U)
        singerlist.append([L,U])
    tourneyscore(singerlist)
