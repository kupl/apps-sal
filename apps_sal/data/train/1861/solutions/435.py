class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        collection = collections.defaultdict(list)
        for x, y in points:
            collection[x].append(y)
        result = float('inf')
        previousx = {}
        for x in sorted(collection):
            column = collection[x]
            column.sort()
            for j, y2 in enumerate(column):
                
                for i in range(j):
                    
                    y1 = column[i]
                    if (y1, y2) in previousx:
                        result = min(result, ((x-previousx[y1,y2]) * (y2-y1)))
                                     
                    previousx[y1,y2] = x
                                    
        if result < float('inf'):
               return result
        return 0
                                
            

