class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_len, target_len, stamp, target, result = len(stamp), len(target), list(stamp), list(target), []
        changed = True
        while changed:
            changed = False
            for i in range(target_len - stamp_len + 1):
                changed |= self.check(stamp, target, i, result)
        return result[::-1] if target == ['?'] * target_len else []   
    
    def check(self, stamp, target, i, result):
        changed = False
        for j in range(len(stamp)):
            if target[i+j] == '?': continue
            if stamp[j] != target[i+j]: return False
            changed = True
        if changed:
            target[i:i+len(stamp)] = ['?'] * len(stamp)
            result.append(i)
        return changed
