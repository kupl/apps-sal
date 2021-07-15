from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d=defaultdict(list)
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        ans=[]
        for i in range(1,max(groupSizes)+1):
            if i in d:
                for j in range(0,len(d[i]),i):
                    ans.append(d[i][j:j+i])
        return ans
        

