class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        if len(S) < 2: return []
    
        def dfs(s, path):
            if not s:
                if len(path) >= 3:
                    return path
                return []

            for  i in range(len(s)):
                if (len(s[:i+1]) > 1 and s[0]==\"0\") or int(s[:i+1]) > 2**31-1:
                    continue 
                if len(path) < 2:
                    tmp = dfs(s[i+1:], path + [s[:i+1]])
                    if tmp:
                        return tmp
                else:
                    if int(path[-2]) + int(path[-1]) == int(s[:i+1]):
                        tmp = dfs(s[i+1:], path +[s[:i+1]])
                        if tmp:
                            return tmp
            return []
        
        return dfs(S,[])
