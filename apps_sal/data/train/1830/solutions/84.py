class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = []
        lakes = {}
        freeDays = []
        for i in range(0, len(rains)):
            if rains[i] != 0:
                if rains[i] not in lakes:
                    lakes[rains[i]] = []
                    lakes[rains[i]].append(0)
                    lakes[rains[i]].append(i)
                elif lakes[rains[i]][0] == 1 and len(freeDays) > 0:
                    for j in range(0, len(freeDays)):
                        if freeDays[j] > lakes[rains[i]][1]:
                            ans[freeDays[j]] = rains[i]
                            lakes[rains[i]][0] -= 1
                            lakes[rains[i]][1] = i
                            freeDays.pop(j)
                            break
                lakes[rains[i]][0] += 1
                lakes[rains[i]][1] = i
                if lakes[rains[i]][0] > 1:
                    return []
                ans.append(-1)
            else:
                freeDays.append(i)
                ans.append(1)
        return ans
