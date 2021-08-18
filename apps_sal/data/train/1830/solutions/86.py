class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = {}
        zeroes = []

        length = len(rains)

        for i, rain in enumerate(rains):
            if rain == 0:
                zeroes.append(i)
                continue

            if rain in lakes:
                lake_index = lakes[rain]

                found = False

                for j, zero in enumerate(zeroes):
                    if zero > lake_index:
                        rains[zero] = rain
                        found = True
                        del zeroes[j]
                        break

                if not found:
                    return []

                lakes[rain] = i
                rains[i] = -1
            else:
                lakes[rain] = i
                rains[i] = -1

        for zero in zeroes:
            rains[zero] = 1

        return rains
