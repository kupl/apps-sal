class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def backtrack(path=[], i=0):
            if i == len(S): return path if len(path) >= 3 else []
            for j in range(i+1, min(i+10, len(S)) + 1):
                if S[i] == '0' and j > i + 1: continue
                x = int(S[i:j])
                if x < 2**31 and (len(path) < 2 or (len(path) >= 2 and x == sum(path[-2:]))):
                    new = backtrack(path + [x], j)
                    if new: return new
            return []
        
        return backtrack()
