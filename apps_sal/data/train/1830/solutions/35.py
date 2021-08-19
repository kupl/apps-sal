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
                # print(f\"Append {day} to dry days\")
                dry_days.append(day)
                ans.append(1)
            else:
                if lake not in full_lakes:
                    # print(f\"Fill lake {lake} at day {day}\")
                    full_lakes[lake] = day
                elif dry_days:
                    filled_at = full_lakes[lake]
                    index = bisect.bisect_right(dry_days, filled_at)
                    # print(f\"Dry days are {dry_days}\")
                    # print(f\"Try to empty lake {lake} filled at day {filled_at}\")

                    if index == len(dry_days):
                        # print(f\"Can't find a dry day to empty lake {lake}\")
                        return list()

                    # print(f\"Use day {dry_days[index]} to empty lake {lake}\")

                    ans[dry_days[index]] = lake
                    del dry_days[index]
                    full_lakes[lake] = day
                else:
                    return list()

                ans.append(-1)

        return ans
