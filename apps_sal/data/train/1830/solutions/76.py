class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ret = [1] * len(rains)
        filled = dict()
        dryDays = list()
        for ind, rain in enumerate(rains):
            if rain > 0:
                ret[ind] = -1
                if rain not in filled:
                    ret[ind] = -1
                    filled[rain] = ind
                    continue
                else:
                    if not dryDays:
                        return []
                    found = False
                    print(ind)
                    for day in dryDays:
                        if day > filled[rain]:
                            ret[day] = rain
                            dryDays.remove(day)
                            found = True
                            filled[rain] = ind
                            break
                    if not found:
                        return []
            else:
                dryDays.append(ind)
        return ret
