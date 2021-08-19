from collections import defaultdict
from bisect import bisect_left, bisect_right


class MajorityChecker:
    def __init__(self, arr):

        # key   : number
        # value : list of indices for number
        self.num_idx_dict = defaultdict(list)

        # Append index to corresoinding number's dictionary
        for idx, number in enumerate(arr):

            self.num_idx_dict[number].append(idx)

        # With descending order of number of occurrences
        self.candidates = sorted(self.num_idx_dict, key=lambda x: len(self.num_idx_dict[x]), reverse=True)

    def query(self, left, right, threshold):

        for number in self.candidates:

            # Longest occurrences is smaller than threhsold, then no solution
            if len(self.num_idx_dict[number]) < threshold:
                return -1

            left_idx = bisect_left(self.num_idx_dict[number], left)
            right_idx = bisect_right(self.num_idx_dict[number], right)

            if right_idx - left_idx >= threshold:
                return number

        return -1
