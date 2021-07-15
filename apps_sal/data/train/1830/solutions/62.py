class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # To be improved with binary search for faster determination of idx for dry
        full, idxDry, res = dict(), [], [-1] * len(rains)
        for i, x in enumerate(rains):
            if not x: idxDry.append(i); continue
            if x in full:
                if not idxDry or full[x] > idxDry[-1]: return []
                # Improve here
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
