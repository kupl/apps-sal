class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        self.RED = 1
        self.BLUE = -1
        self.result = [float(\"inf\")] * n
        self.result[0] = 0
        self.n = n
        self.dp = [[None] * n for _ in range(n)]
        self.visited = set()
        
        for e in red_edges:
            if self.dp[e[0]][e[1]] == None:
                self.dp[e[0]][e[1]] = list()
            self.dp[e[0]][e[1]].append(self.RED)
            
        for e in blue_edges:
            if self.dp[e[0]][e[1]] == None:
                self.dp[e[0]][e[1]] = list()
            self.dp[e[0]][e[1]].append(self.BLUE)
        
        
        q = [[0, -1], [0, 1]]
        num = 0
        
        while(len(q)):
            size = len(q)
            num += 1
            
            for _ in range(size):
                cur = q.pop(0)
                node = cur[0]
                op_c = cur[1]
                
                for i in range(1, n):
                    if self.dp[node][i] != None and op_c in self.dp[node][i]:
                        if (str(i) + str(op_c)) not in self.visited:
                            self.visited.add(str(i) + str(op_c))
                            self.result[i] = min(self.result[i], num)
                            q.append([i, op_c * -1])
                
        return [x if x != float(\"inf\") else -1 for x in self.result]
                
        
    def prettyPrint(self, dp):
        for row in dp:
            print(row)
            
            
