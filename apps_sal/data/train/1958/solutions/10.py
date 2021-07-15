import collections
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        d = collections.defaultdict(list)
        out = []
        
        for i,ele in enumerate(groupSizes):
            
            d[ele].append(i)
            print(d)
            if len(d[ele]) == ele:
                    out.append(d[ele])
                    del d[ele]
        return out

