class Solution(object):
    def minAreaRect(self, points):
        y_group=collections.defaultdict(list)
        for x, y in points:
            y_group[x].append(y)
            
        visited={}
        area=inf
        
        for x in sorted(y_group):
            Y=y_group[x]
            Y.sort()
            for i in range(len(Y)):
                y1= Y[i]
                for j in range(i):
                    y2=Y[j]
                    if (y1, y2) in visited:
                        area=min((x - visited[(y1, y2)])* (y1 - y2), area)
                    visited[(y1, y2)]=x
        return area if area<inf else 0
                    

