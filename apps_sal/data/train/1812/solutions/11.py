from collections import defaultdict
from bisect import bisect_left, bisect_right


class MajorityChecker:
    def __init__(self, arr):

        self.num_idx_dict = defaultdict(list)

        for idx, number in enumerate(arr):

            self.num_idx_dict[number].append(idx)

        self.candidates = sorted(self.num_idx_dict, key=lambda x: len(self.num_idx_dict[x]), reverse=True)

    def query(self, left, right, threshold):

        for number in self.candidates:

            if len(self.num_idx_dict[number]) < threshold:
                return -1

            left_idx = bisect_left(self.num_idx_dict[number], left)
            right_idx = bisect_right(self.num_idx_dict[number], right)

            if right_idx - left_idx >= threshold:
                return number

        return -1
