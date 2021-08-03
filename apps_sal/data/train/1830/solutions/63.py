from bisect import bisect_left


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        filled = {}
        ans = [-1] * len(rains)
        rem = []

        def get(r):  # idx for first zero b4 right
            low, high = 0, len(rem) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if rem[mid] > r:
                    low = mid + 1
                else:
                    high = mid - 1
            # print(low)
            return rem[low] if 0 <= low < len(rem) else -1

        for i in range(len(rains) - 1, -1, -1):
            curr = rains[i]
            # if i == 8:
            #     print(rem)
            if curr == 0:
                rem.append(i)
                continue
            elif curr in filled:
                if not rem:
                    return []

                idx = filled.pop(curr)
                zero = get(idx)

                if not i < zero < idx:
                    # print(rem)
                    # print(curr, i, zero, idx)
                    return []
                ans[zero] = curr
                rem.remove(zero)

            filled[curr] = i
        while rem:
            ans[rem.pop()] = 1
        return ans
