class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # Time: O(T(T-S)*S); Space: O(S) #
        # We iteratively find the stamp in target and replace the matched string to * 
        # we need to reverse the ans, because the first find ones would be the one that final filled as the assume target at begining is filled with all \"?\"
        # we are filling it back
        
        M, N = len(stamp), len(target)
        stamp = list(stamp)
        target = list(target)
        ans = []
        
        def check(i):
            changed = False
            for j in range(M):
                if target[i+j] == \"?\":
                    continue
                if target[i+j] != stamp[j]:
                    return False
                changed = True
            if changed:
                target[i:i+M] = [\"?\"]*M
                ans.append(i)
            return changed
        
        changed = True
        while changed:
            changed = False
            for i in range(N - M + 1):
                changed = changed or check(i)
        return ans[::-1] if target == [\"?\"]*N else []
