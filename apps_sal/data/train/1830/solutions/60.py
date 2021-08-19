from bisect import bisect_left


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        flooded = {}
        dry_days = []
        out = [-1 for _ in range(len(rains))]

        for i in range(len(rains)):
            day = rains[i]
            if day > 0:
                if day in flooded:
                    if dry_days:
                        # found = False
                        # for d in range(len(dry_days)):
                        #     dry_day = dry_days[d]
                        #     if dry_day > flooded[day]:
                        #         out[dry_day] = day
                        #         dry_days.pop(d)
                        #         found = True
                        #         break
                        # if not found:
                        #     return []
                        dry = bisect_left(dry_days, flooded[day])
                        if dry == len(dry_days):
                            return []
                        else:
                            dry_day = dry_days.pop(dry)
                            out[dry_day] = day
                    else:
                        return []
                flooded[day] = i
            else:
                dry_days.append(i)
        for dry_day in dry_days:
            out[dry_day] = 1
        return out
