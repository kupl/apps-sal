class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        self.red = {}
        self.blue = {}
        for u,v in red_edges:
            if u not in self.red:
                self.red[u]=[]
            self.red[u].append(v)
            
        for u,v in blue_edges:
            if u not in self.blue:
                self.blue[u]=[]
            self.blue[u].append(v)
        
        
        def visit(i):
            if i == 0:
                return 0
            color = [self.red,self.blue]
            q = [(0,0),(0,1)]
            n=0
            visited = {}
            while len(q)>0:
                n+=1
                nxt = []
                for u,c in q: visited[(u,c)] = True
                while len(q)>0:
                    u,c = q.pop()
                    if c == 0:
                        if u in color[1]:
                            for v in color[1][u]:
                                if (v,1) not in visited:
                                    if v == i:
                                        return n
                                    else:
                                        nxt.append((v,1))
                    if c == 1:
                        if u in color[0]:
                            for v in color[0][u]:
                                if (v,0) not in visited:
                                    if v == i:
                                        return n
                                    else:
                                        nxt.append((v,0))
                q = nxt
            
            return -1
                    
                    
        result = []           
        for i in range(n):
            d = visit(i)
            result.append(d)
        return result
