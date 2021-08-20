from collections import deque


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        zero_indices = deque()
        last_flood = {}
        result = [-1] * len(rains)

        def find_zero_for_lake(idx, r):
            if not zero_indices:
                return None
            for zero_index in zero_indices:
                if last_flood[r] < zero_index < idx:
                    return zero_index
            return None
        for (idx, r) in enumerate(rains):
            if r > 0:
                if r in last_flood:
                    found_zero = find_zero_for_lake(idx, r)
                    if found_zero is None:
                        return []
                    else:
                        result[found_zero] = r
                        zero_indices.remove(found_zero)
                last_flood[r] = idx
            else:
                zero_indices.append(idx)
        while zero_indices:
            zero_index = zero_indices.pop()
            result[zero_index] = 1
        return result
