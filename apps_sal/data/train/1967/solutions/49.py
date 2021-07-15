class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        if len(S) < 2: return []
    
        def dfs(s, path, res):

            if not s:
                if len(path) >= 3:
                    res.append(path)
                    if not res:
                        return 

            for  i in range(len(s)):
                
                if (len(s[:i+1]) > 1 and s[0]==\"0\") or int(s[:i+1]) > 2**31-1:
                    continue 
                    
                if len(path) < 2:
                    dfs(s[i+1:], path + [s[:i+1]], res)
                else:
                    if int(path[-2]) + int(path[-1]) == int(s[:i+1]):
                        dfs(s[i+1:], path +[s[:i+1]], res)
        res = []               
        dfs(S,[], res)
        return res[0] if res else []
