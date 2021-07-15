from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        ref_x = defaultdict(list)
        ref_y = defaultdict(list)
        
        for point in points:
            x, y = point[0], point[1]
            ref_x[x].append(y)
            ref_y[y].append(x)
            
        print(\"ref_x={}\".format(ref_x))
        print(\"ref_y={}\".format(ref_y))
        
        ans = float('inf')
        for x in ref_x.keys():
            if len(ref_x[x]) < 2:
                continue
            
            ys = sorted(ref_x[x])
            for i in range(len(ys)-1):
                first_y = ys[i]
                if len(ref_y[first_y]) < 2:
                    continue
                for j in range(i+1, len(ys)):
                    second_y = ys[j]
                    if len(ref_y[second_y]) < 2:
                        continue
                    
                    second_xs = list(set(ref_y[first_y]).intersection(set(ref_y[second_y])))
                    if not second_xs:
                        continue
                    
                    for second_x in second_xs:
                        #print(\"first_x={} second_x={} first_y={} second_y={} res={}\".format(x, second_x, first_y, second_y, abs(x-second_x)*abs(first_y-second_y)))
                        if x != second_x and first_y != second_y:
                            ans = min(ans, abs(x-second_x)*abs(first_y-second_y))
                        
        return ans if ans < float('inf') else 0
                
        
