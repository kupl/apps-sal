class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        op = []
        lakes = dict()
        days = []
        for (i, r) in enumerate(rains):
            if r > 0:
                op.append(-1)
                if r in lakes.keys():
                    day = lakes[r]
                    v = -1
                    for d in days:
                        if d > day:
                            v = d
                            break
                    if v > 0:
                        days.remove(v)
                        op[v] = r
                    else:
                        return []
                lakes[r] = i
            else:
                op.append(99999)
                days.append(i)
        return op
