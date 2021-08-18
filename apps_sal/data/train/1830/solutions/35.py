from typing import Set, List
from copy import deepcopy
import bisect


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lakes = dict()
        dry_days = list()
        ans = list()

        for day, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(day)
                ans.append(1)
            else:
                if lake not in full_lakes:
                    full_lakes[lake] = day
                elif dry_days:
                    filled_at = full_lakes[lake]
                    index = bisect.bisect_right(dry_days, filled_at)

                    if index == len(dry_days):
                        return list()

                    ans[dry_days[index]] = lake
                    del dry_days[index]
                    full_lakes[lake] = day
                else:
                    return list()

                ans.append(-1)

        return ans
