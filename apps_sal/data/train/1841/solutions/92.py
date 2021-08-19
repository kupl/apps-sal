class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        medVal = sorted(arr)[(len(arr) - 1) // 2]
        return sorted(arr, key=lambda x: [abs(x - medVal), x], reverse=True)[:k]
        '\n        sList = sorted(arr)\n        medianIndex = (len(arr)-1) // 2\n        medianValue = sList[medianIndex]\n        \n        strongList = [(abs(elem - medianValue), elem) for elem in sList]\n        #finalList = sorted(strongList, reverse = True, key=lambda x:x[0])\n        ht = {}\n        returnList = []\n        for elem in strongList:\n            if elem[0] in ht:\n                ht[elem[0]].append(elem[1])\n            else:\n                ht[elem[0]] = [elem[1]]\n                \n        for key in ht:\n            curr = sorted(ht[key], reverse = True)\n            returnList.append((key, curr))\n \n        finalList = sorted(returnList, reverse = True, key=lambda x:x[0])\n        newList = [elem[1] for elem in finalList]\n        newerList = [i for elem in newList for i in elem]\n        \n        return newerList[:k]\n        '
