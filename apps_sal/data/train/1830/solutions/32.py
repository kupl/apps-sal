class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full = set()
        drys = []
        filled = {}
        for i in range(len(rains)):
            if not rains[i]:
                drys.append(i)
            else:
                if rains[i] in full:
                    if not drys:
                        return []
                    if drys[-1] < filled[rains[i]]:
                        return []
                    index = bisect.bisect(drys, filled[rains[i]])
                    rains[drys.pop(index)] = rains[i]
                else:
                    full.add(rains[i])
                filled[rains[i]] = i
                rains[i] = -1
        rains = [1 if i == 0 else i for i in rains]
        return rains
