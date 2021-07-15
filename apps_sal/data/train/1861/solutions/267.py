class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        y_in_x = defaultdict(list)
        x_in_vline = defaultdict(list)
        ans = float(\"inf\")
        for x,y in points:
            if len(y_in_x[x]) >= 1 :
                for pre_y in y_in_x[x]:
                    a,b = max(pre_y,y) , min(pre_y,y)
                    if len(x_in_vline[(a,b)]) >= 1:
                        for pre_x in x_in_vline[(a,b)]:
                            ans = min(ans,(a-b)*abs(x-pre_x))
                    x_in_vline[(a,b)].append(x)
            y_in_x[x].append(y)
        
        #print(y_in_x)
        #print(x_in_vline)
        return ans if ans < float(\"inf\") else 0
