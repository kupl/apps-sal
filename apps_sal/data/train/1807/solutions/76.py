class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            if a<b: return gcd(b, a)
            while b>0:
                tmp = a % b
                a=b
                b=tmp
            return a
##        print(gcd(89,6))
        ans=[]
        if -1<n<2:return ans
        for i in range(1,n):
            for j in range(i+1,n+1):#pass
                if i!=j:
                    x=gcd(i,j)
##                    print(i,j,x)
##                    print(x)
                    n1=i
                    n2=j
                    if i%x==0==j%x and x>1:
                        n1//=x
                        n2//=x
##                    st=(i,j)
##                    print(st)
                    st=f'{n1}/{n2}'
                    if st not in ans:
                        ans.append(st)
##        ans.sort()
##        print(ans)
##        for i,an in enumerate(ans):
##            ans[i]=f'{an[0]}/{an[1]}'
                        
        return ans
