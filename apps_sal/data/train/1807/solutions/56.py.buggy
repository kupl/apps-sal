class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result=[]
        if n == 1:
            return(result)
        for i in range(2,n+1):
            result.append(\"1/\"+str(i))
            for j in range(2,i):
                flag=0
                for k in range(2,j+1):
                    if j%k==0:
                        if i%k ==0:
                            flag=flag+1
                if flag == 0:
                    result.append(str(j)+\"/\"+str(i))
        return(result)
