class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
#         res = []
#         self.dfs(res, S, [])
#         return res[0] if res else []
    
#     def dfs(self, res, S, path):
#         if len(path) >= 3 and not S:
#             res.append(path[:])
#             return True
        
#         for i in range(1, len(S)+1):
#             if i > 1 and S[0] == '0' or int(S[:i]) > 2**31-1:
#                 return
#             if len(path) <= 1:
#                 path.append(int(S[:i]))
#                 if self.dfs(res, S[i:], path):
#                     return True
#                 path.pop()
#             elif path[-1] + path[-2] == int(S[:i]):
#                 path.append(int(S[:i]))
#                 if self.dfs(res, S[i:], path):
#                     return True
#                 path.pop()
                
        # second try
        res = []
        self.dfs(res, S, 0, [])
        return res[0] if res else []
    
    def dfs(self, res, S, index, path):
        # print(path)
        if index == len(S) and len(path) >= 3:
            res.append(path[:])
            return
        
        for i in range(index+1, len(S)+1):
            if (i > index + 1 and S[index] == '0') or int(S[index:i]) > 2**31 - 1:
                return
            temp_num = int(S[index:i])
            if (len(path) >= 2 and temp_num == path[-1] + path[-2]) or len(path) < 2:
                path.append(temp_num)
                self.dfs(res, S, i, path)
                path.pop()


