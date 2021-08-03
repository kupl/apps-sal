class Solution:
    # O(mnn) time, O(n) space
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        target_list = list(target)
        result = []
        
        def is_changed(i):
            changed = False
            for j in range(m):
                if target_list[i + j] == \"?\":
                    continue
                if target_list[i + j] != stamp[j]:
                    return False
                # equal to stamp[j] and should be changed to ?
                changed = True
            if changed:
                for j in range(m):
                    target_list[i + j] = \"?\"
                result.append(i)
            return changed
        
        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= is_changed(i)
        
        if all(x == \"?\" for x in target_list):
            return result[::-1]
        return []
