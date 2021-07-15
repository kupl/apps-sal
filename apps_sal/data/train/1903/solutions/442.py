class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        vertices = {}
        x, y = points[0][0], points[0][1]
        
        for u, v in points: 
            vertices[(u, v)] = abs(u - x) + abs(v - y)
            
        def mindistance() -> tuple:
            
            Node = None
            
            for node in vertices:
                
                if not Node: Node = node
                elif vertices[node] < vertices[Node]: Node = node
            
            return Node
        
        n = len(points)
        Cost = 0
        
        for i in range(n):
            
            temp = mindistance()
            Cost += vertices[temp]
            vertices.pop(temp)
            
            for c in vertices:
                vertices[c]  = min(vertices[c], abs(c[0] - temp[0]) + abs(c[1] - temp[1]))
                
        return Cost
                    
            

