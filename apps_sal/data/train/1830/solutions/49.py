class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        spares = []
        full = {}
        for i in range(len(rains)):
            if rains[i] > 0:
                if rains[i] in full:
                    for j in range(len(spares)):
                        if spares[j] > full[rains[i]]:
                            ans[spares.pop(j)] = rains[i]
                            full[rains[i]] = i
                            break
                    else:
                        return []
                else:
                    full[rains[i]] = i
            else:
                spares.append(i)
        for i in spares:
            ans[i] = 1
        return ans
