class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        col = defaultdict(list)
        
        for x, y in points:
            col[x].append(y)
        
        res = float('inf')
        
        pre = defaultdict(int)
        for x in sorted(col):
            col[x].sort()
            for i in range(len(col[x]) - 1):
                for j in range(i + 1, len(col[x])):
                    if (col[x][i], col[x][j]) in pre:
                        res = min(res, (col[x][j] - col[x][i]) * (x - pre[(col[x][i], col[x][j])]))
                    pre[(col[x][i], col[x][j])] = x
        
        return (res if res != float('inf') else 0)
