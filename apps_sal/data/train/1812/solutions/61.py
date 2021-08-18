from collections import defaultdict
import bisect


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.pos = defaultdict(list)
        self.count = defaultdict(int)
        for i in range(len(arr)):
            item = arr[i]
            self.pos[item].append(i)
            self.count[item] += 1
        self.rank = sorted(list(self.count.keys()), key=lambda x: self.count[x], reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:

        if right - left < 40:
            dp = defaultdict(int)
            for i in range(left, right + 1):
                dp[self.arr[i]] += 1
            element = max(list(dp.keys()), key=lambda x: dp[x])
            if dp[element] >= threshold:
                return element
            else:
                return -1
        else:
            for item in self.rank:
                if self.count[item] >= threshold:
                    l1 = bisect.bisect_left(self.pos[item], left)
                    l2 = bisect.bisect_right(self.pos[item], right)
                    if l2 - l1 >= threshold:
                        return item
                else:
                    break
            return -1
