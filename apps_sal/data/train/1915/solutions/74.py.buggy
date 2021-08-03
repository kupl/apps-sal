class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        S = list(stamp)
        T = list(target)
        visited = [False for _ in range(len(T))]
        ans = []
        cnt = 0
        while cnt < len(T):
            found = False
            for i in range(len(T) - len(S) + 1):
                if not visited[i] and self.canStamp(S, T, i):
                    cnt += self.doStamp(S, T, i)
                    found = True
                    ans.append(i)
                    visited[i] = True
                    break
            if not found:
                return []
        return ans[::-1]
    
    
    def canStamp(self, S, T, start):
        for i in range(len(S)):
            if S[i] != T[i+start] and T[i+start] != \"?\":
                return False
        return True
    
    def doStamp(self, S, T, start):
        cnt = 0
        for i in range(len(S)):
            if T[i + start] != \"?\":
                cnt += 1
                T[i + start] = \"?\"
        return cnt
