class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        (full, idxDry, res) = (dict(), [], [-1] * len(rains))
        for (i, x) in enumerate(rains):
            if not x:
                idxDry.append(i)
                continue
            if x in full:
                if not idxDry or full[x] > idxDry[-1]:
                    return []
                for idx in idxDry:
                    if idx > full[x]:
                        res[idx] = x
                        idxDry.remove(idx)
                        del full[x]
                        break
            full[x] = i
        for i in idxDry:
            res[i] = 1
        return res
