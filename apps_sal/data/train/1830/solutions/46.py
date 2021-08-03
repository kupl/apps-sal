class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        drying = []
        out = []
        lakes = {}
        v = 1
        for c, i in enumerate(rains):
            out.append(-1)
            if i <= 0:
                drying.append(c)
            elif i in lakes and drying:
                found = -1
                for index, val in enumerate(drying):
                    if val > lakes[i]:
                        found = index
                        break
                if found > -1:
                    out[drying.pop(found)] = i
                    lakes[i] = c
                else:
                    return []
            elif i in lakes:
                return []
            else:
                lakes[i] = c
                v = i
        for j in drying:
            out[j] = v
        return out
