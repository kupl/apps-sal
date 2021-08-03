class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        d = {}
        dry = []
        res = []
        for day, rain in enumerate(rains):
            if rain != 0:
                if rain in d:
                    p = d[rain]
                    flag = -1
                    for dry_day in dry:
                        if dry_day > p:
                            flag = dry_day
                            break
                    if flag == -1:
                        return []
                    res[flag] = rain
                    dry.remove(flag)
                    d[rain] = day
                else:
                    d[rain] = day
                res.append(-1)
            else:
                dry.append(day)
                res.append(56)
        return res
