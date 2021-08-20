class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        free_days = []
        lake_tracker = {}
        free_days_balance = 0
        ans = [-1 if rains[i] > 0 else 1 for i in range(len(rains))]
        for i in range(len(rains)):
            if rains[i] > 0:
                lake = rains[i]
                if lake in lake_tracker:
                    if free_days_balance > 0:
                        index = lake_tracker[lake]
                        fnd = None
                        for free_day in free_days:
                            if index < free_day:
                                fnd = free_day
                                break
                        if not fnd:
                            return []
                        free_days_balance = free_days_balance - 1
                        lake_tracker[lake] = i
                        ans[fnd] = lake
                        free_days.remove(fnd)
                    else:
                        return []
                else:
                    lake_tracker[lake] = i
            else:
                free_days_balance = free_days_balance + 1
                free_days.append(i)
        return ans
