class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        self.color = {}
        self.adj = {}
        for x,y in dislikes:
            if x not in self.adj:
                self.adj[x] = []
            if y not in self.adj:
                self.adj[y] = []
            self.adj[x].append(y)
            self.adj[y].append(x)
            
        self.flag = True
        def visit(x,c):
            self.color[x] = c
            if c == 0:
                n_c = 1
            else:
                n_c = 0
            for y in self.adj[x]:
                if y not in self.color:
                    visit(y,n_c)
                else:
                    if self.color[y] == c:
                        self.flag = False
        for x,y in dislikes:
            if x not in self.color:
                visit(x,0)
            if y not in self.color:
                visit(y,0)
        return self.flag

