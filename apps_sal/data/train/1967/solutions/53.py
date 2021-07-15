class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        N = 2 ** 31 - 1
        
        def dfs(s, path, res):
            if not s and len(path) > 2:
                res.append(path)
                return
            for i in range(len(s)):
                if len(s[:i + 1]) != len(str(int(s[:i + 1]))) or int(s[:i + 1]) > N: continue
                if len(path) < 2: dfs(s[i + 1:], path + [s[:i + 1]], res)
                elif len(path) > 1 and int(s[:i + 1]) == int(path[-1]) + int(path[-2]):
                    dfs(s[i + 1:], path + [s[:i + 1]], res)
        
        res, ans = [], []
        dfs(S, [], res)
        if not res: return []
        for elem in res[0]:
            ans.append(int(elem))
        return ans
            

