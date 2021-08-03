class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        if len(S) < 3: return []
        
        def dfs(S, path):
            if not S:
                if len(path) >= 3:
                    return path
                return []
                
            for l in range(1, len(S) + 1):
                if (len(S[:l]) > 1 and S[0] == \"0\") or (int(S[:l]) > 2**31 -1):
                    continue 
                    
                if len(path) < 2:
                    temp = dfs(S[l:], path + [int(S[:l])])
                    if temp:
                        return temp
                    
                else:
                    if path[-1] + path [-2] == int(S[:l]):
                        temp = dfs(S[l:], path + [int(S[:l])])
                        if temp:
                            return temp
            return []
        
        return dfs(S, [])
                
                        
            
