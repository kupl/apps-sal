class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        zeros = []
        last = {}
        ans = [-1] * len(rains)

        for i in range(len(rains)):
            if rains[i] == 0:
                ans[i] = 1

        for i, lake in enumerate(rains):
            if lake == 0:
                zeros.append(i)
            else:
                if lake in last:
                    prev_idx = last[lake]
                    zero = bisect_left(zeros, prev_idx)
                    if zero < len(zeros):
                        # found a valid lake
                        zero_lake = zeros.pop(zero)
                        last[lake] = i
                        ans[zero_lake] = lake
                    else:
                        return []
                else:
                    last[lake] = i
        return ans
