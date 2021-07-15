class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ones = set([])
        start = []
        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ones.add((i, j))
                    start.append([(i, j), grid[i][j], set([(i, j)])])
                    answer = max(answer, grid[i][j])
        nearby = {}
        for a, b in ones:
            nearby[(a, b)] = []
            for c, d in [(a+1, b), (a-1, b), (a, b-1), (a, b+1)]:
                if (c, d) in ones:
                    if (a==c and abs(b-d)==1) or (abs(a-c)==1 and b==d):
                        nearby[(a, b)].append((c, d))
        while True:
            next = []
            for a, b, c in start:
                for a2 in nearby[a]:
                    if a2 not in c:
                        b2 = b+grid[a2[0]][a2[1]]
                        c2 = c.union(set([a2]))
                        answer = max(answer, b2)
                        next.append([a2, b2, c2])
            start = next
            if len(start)==0:
                break
        return answer
                        
                        
        
                                  
                    

