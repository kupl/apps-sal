class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
#         if n == 1:
#             return []
        
        results = []
        fractions = []
        for i in range(1, n+1):
            for j in range(1, i+1):
                tmp = j/i
                # if tmp >= 1:
                    # break
                if tmp not in results and tmp < 1:
                    results.append(tmp)
                    fractions.append(\"{}/{}\".format(j, i))
        return fractions   

#         fractions = []
#         decimals = set()
        
#         for i in range(1, n + 1):
#             for x in range (1, i + 1):
#                 if (x % i != 0 and x/i not in decimals):
#                     decimals.add(x/i)
#                     fractions.append(str(x) + \"/\" + str(i))
                    
#         return fractions
    
# a = Solution()
# res = a.simplifiedFractions(4)
# print(res)
