class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        medVal = sorted(arr)[(len(arr) - 1) // 2]
        return sorted(arr, key=lambda x: [abs(x - medVal), x], reverse=True)[:k]

        '''
        sList = sorted(arr)
        medianIndex = (len(arr)-1) // 2
        medianValue = sList[medianIndex]
        
        strongList = [(abs(elem - medianValue), elem) for elem in sList]
        ht = {}
        returnList = []
        for elem in strongList:
            if elem[0] in ht:
                ht[elem[0]].append(elem[1])
            else:
                ht[elem[0]] = [elem[1]]
                
        for key in ht:
            curr = sorted(ht[key], reverse = True)
            returnList.append((key, curr))
 
        finalList = sorted(returnList, reverse = True, key=lambda x:x[0])
        newList = [elem[1] for elem in finalList]
        newerList = [i for elem in newList for i in elem]
        
        return newerList[:k]
        '''
