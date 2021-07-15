'''
We can group them in group of X's, using dictionary

So we loop through all Y's in xs and keep track of the X of last seen pair of Y. We can hash Y's and keep dictionary of pair. Each time we find pair that already exist, we document their solution. 

Complexity:
So if there are N points and each column has K points. So there are N/K columns. We loop through each column, for each column we loop through k points twice. So N/K * K * K so = Nk

O(Nk) but K could be N so O(N^2)
O(N)
'''
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xD = collections.defaultdict(list)
        for x, y in points:
            xD[x].append(y)
        
        sol = math.inf
        lastSeen = collections.defaultdict(int)
        for x in sorted(xD.keys()):
            for i1 in range(len(xD[x])):
                for i2 in range(i1 + 1, len(xD[x])):
                    
                    pair1,pair2, diff = (xD[x][i1], xD[x][i2]), (xD[x][i2], xD[x][i1]),abs(xD[x][i1]-xD[x][i2])
                    if pair1 in lastSeen or pair2 in lastSeen:
                        sol = min(diff * (x-lastSeen[pair1]), sol)
                    lastSeen[pair1], lastSeen[pair2] = x,x
        return sol if sol != math.inf else 0
                        
                        
                
                        

