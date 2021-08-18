class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        dpcache = {}
        distance = 0

        for el1 in arr1:
            if dpcache.get(el1) is True:
                distance += 1
                continue
            elif dpcache.get(el1) is False:
                continue
            else:
                pass

            for el2_idx, el2 in enumerate(arr2):
                if abs(el1 - el2) <= d:
                    dpcache[el1] = False
                    break

                if el2_idx == len(arr2) - 1:
                    dpcache[el1] = True
                    distance += 1

        return distance
