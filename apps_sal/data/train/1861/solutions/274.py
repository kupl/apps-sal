class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        point_dict = {}
        point_list = []
        
        for i in points:
            point_dict[(i[0],i[1])] = 1
            point_list.append((i[0],i[1]))
            
        print(point_dict)
        print(point_list)
        
        ans = math.inf
        for i in range(0,len(points)):
            for j in range(i,len(points)):
                ix, iy = point_list[i]
                jx, jy = point_list[j]
                if ix==jx or iy==jy:
                    continue
                if ((ix,jy) in point_dict) and ((jx,iy) in point_dict):
                    ans = min(ans,abs(ix-jx)*abs(iy-jy))

        if ans == math.inf:
            return 0
        return ans
