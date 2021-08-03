from collections import deque


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_sequence = [1 for _ in range(len(rains))]
        full_lakes = {}
        dry_days = deque()
        for i, lake in enumerate(rains):
            if lake:
                dry_sequence[i] = -1
                if lake in full_lakes:
                    if dry_days:
                        index = 0
                        while index < len(dry_days) and dry_days[index] <= full_lakes[lake]:
                            index += 1
                        if index < len(dry_days):
                            dry_sequence[dry_days[index]] = lake
                            del dry_days[index]
                        else:
                            return []
                    else:
                        return []
                full_lakes[lake] = i
            else:
                dry_days.append(i)
        return dry_sequence
