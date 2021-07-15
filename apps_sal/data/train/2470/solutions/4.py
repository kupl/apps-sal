class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
#         for i in range(len(dominoes)-1):
#             for j in range(i+1,len(dominoes)):
#                 if (dominoes[i][0]==dominoes[j][0] and dominoes[i][1]==dominoes[j][1] ) or (dominoes[i][0]==dominoes[j][1] and dominoes[i][1]==dominoes[j][0] ):
#                     count+=1
                    
#         return count
    
        mydict = {}
        for dom in dominoes:
            if ''.join(str(dom)) in mydict:
                mydict[''.join(str(dom))] += 1
            elif  ''.join(str(dom[::-1])) in mydict:
                mydict[''.join(str(dom[::-1]))] += 1
            else:
                mydict[''.join(str(dom))] = 1
        for val in list(mydict.values()):
            if val > 1:
                count += val*(val-1)//2

        return count


