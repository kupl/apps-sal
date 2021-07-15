class Solution:
    from collections import defaultdict
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distDict = defaultdict(list)
        
        for point in points:
            dist = point[0]**2 + point[1]**2
            distDict[dist].append(point)
            
        sortedKey = sorted(distDict.keys())
        
        rst = []
        for key in sortedKey:
            numOfPairs = len(distDict[key])
            if(numOfPairs < K):
                K -= numOfPairs
                rst += distDict[key]
            elif(numOfPairs >= K):
                rst += distDict[key][:K]
                return rst
