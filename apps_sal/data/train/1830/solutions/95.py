class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        counter = collections.Counter()
        firstSeen = {}
        empty = [-1] * len(rains)
        sunny = {}
        for (day, lake) in enumerate(rains):
            if lake > 0:
                if counter[lake] >= 1:
                    for index in sunny:
                        if index > firstSeen[lake]:
                            empty[index] = lake
                            counter[lake] -= 1
                            del sunny[index]
                            break
                    if counter[lake] >= 1:
                        return []
                counter[lake] += 1
                firstSeen[lake] = day
            else:
                sunny[day] = 1
        for day in sunny:
            empty[day] = 1
        return empty
