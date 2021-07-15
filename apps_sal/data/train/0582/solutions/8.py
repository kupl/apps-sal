try:
    def findans(s):
        l,val,r=[],{},[]
        for i,kk in enumerate(s):
            if kk == '(':
                l.append(i+1)
            elif l:
                x=l.pop()
                val[x]=i+1
                x-=2
                while x>=0 and s[x]==')':
                    val[x+1]=i+1
                    x-=1
        return val
    
    for ii in range(int(input())):
        b=input()
        dic=findans(b)
        n=int(input())
        q=list(map(int, input().split()))
        for jj in q:
            print(dic.get(jj,-1))
except: pass
