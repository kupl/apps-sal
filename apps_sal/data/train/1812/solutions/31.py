from collections import defaultdict
import bisect


class MajorityChecker:
    # Use a dictionary to store the index of each element in arr and sort the dictionary by the frequence of each value in arr
    # Use bisection search to fix the insertion position of left and right, and compare right-left to the threshold

    def __init__(self, arr: List[int]):
        self.d = defaultdict(list)
        for i, value in enumerate(arr):
            self.d[value].append(i)

        self.d = sorted(list(self.d.items()), key=lambda x: -len(x[1]))

    def query(self, left: int, right: int, threshold: int) -> int:
        for num, idxs in self.d:
            if len(idxs) >= threshold:
                low = bisect.bisect_left(idxs, left)
                high = bisect.bisect_right(idxs, right)
                if (high - low) >= threshold:
                    return num
            else:
                break
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
