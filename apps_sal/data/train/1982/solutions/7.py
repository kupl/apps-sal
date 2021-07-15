class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.ans = True    
    
        def dfs(p, d, ld, l):
            if not self.ans:
                return

            if not p in ld:
                ld[p] = l
            else:
                if ld[p] != l:
                    self.ans = False
                return
                        
            for n in d[p]:
                dfs(n, d, ld, (l + 1) % 2)
        
        i = 0
        d = {}
        while i < len(dislikes):
            [a, b] = dislikes[i]
            if a in d:
                d[a].append(b)
            else:
                d[a] = [b]
            if b in d:
                d[b].append(a)
            else:
                d[b] = [a]
            i += 1
                
        
        ld = {}
        for k in d:
            if not k in ld:
                dfs(k, d, ld, 0)
                if not self.ans: 
                    break
                    
        return self.ans

