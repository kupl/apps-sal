import sortedcontainers


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        ans = [-1] * n

        track = {}
        ptr = 0
        dries = sortedcontainers.SortedList()

        while ptr < n:
            lake = rains[ptr]

            if lake > 0:
                if lake in track:
                    last_rain = track[lake]

                    if not dries:
                        return []

                    idx = dries.bisect_right(last_rain)
                    if idx >= len(dries):
                        return []

                    dry_pos = dries[idx]
                    if dry_pos < last_rain:
                        return []

                    dries.discard(dry_pos)

                    ans[dry_pos] = lake
                    track[lake] = ptr
                else:
                    track[lake] = ptr
            else:
                dries.add(ptr)

            ptr += 1

        for i in dries:
            ans[i] = 1

        return ans
