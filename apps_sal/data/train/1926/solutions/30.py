class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        need1=num+1
        need2=num+2
        
        def factors(num):
            mi=float('inf')
            ans=[]
            for i in range(1,int(num**(0.5))+1):
                if(num%i==0):
                    if(num//i-i<mi):
                        ans=[i,num//i]
                        
            return ans
        
        ls1=factors(need1)
        ls2=factors(need2)
        print((ls1,ls2))
        if(ls1[1]-ls1[0]<ls2[1]-ls2[0]):
            return ls1
        else:
            return ls2
        
        

