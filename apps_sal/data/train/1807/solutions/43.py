class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        def hasFactor(divisor,dividend):
            for  i in range(2,divisor+1):
                if dividend%i==0 and divisor%i==0:
                    return True
            return False
            
        def fractions(result,i):
            for k in range(1,i):
                if k > 1 and hasFactor(k,i):
                    continue
                result.append(str(k)+'/'+str(i))
        
        result = []
        for i in range(2,(n+1)):
            fractions(result,i)
        return result
        print(result)
