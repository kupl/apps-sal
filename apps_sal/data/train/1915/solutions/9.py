class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def one_sweep():
            nonlocal done, ans
            for ti in range(len(target) - len(stamp) + 1):
                matched_cs, matched = [], True
                for si in range(len(stamp)):
                    sc, tc = stamp[si], target[ti]
                    if ti in done:
                        ti = ti + 1
                        continue
                    elif sc == tc:
                        matched_cs.append(ti)
                        ti = ti + 1
                    else:
                        matched = False
                        break
                if matched and matched_cs:
                    done = done | set(matched_cs)
                    ans.append(ti - len(stamp))
                    return True                        
            return False
            
        ans, done = [], set()
        while one_sweep(): pass
        return ans[::-1] if len(done) == len(target) else []

