class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result_str = []
        result_num = []
        for i in range(1, n+1):
            for j in range(1, i):
                if j/i not in result_num:
                    result_num.append(j/i)
                    result_str.append(\"{}/{}\".format(j, i))
        return result_str
                
        
