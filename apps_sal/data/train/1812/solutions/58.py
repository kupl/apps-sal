import collections as clc
import time

start = time.time()


class SegmentTree:

    def __init__(self, left_bound: int, right_bound: int):
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.mid = None
        self.values = None
        self.most_frequent = None
        self.left = None
        self.right = None

    def split(self, mid: int):
        self.mid = mid
        self.left = SegmentTree(self.left_bound, self.mid)
        self.right = SegmentTree(self.mid, self.right_bound)

    def __len__(self):
        return self.right_bound - self.left_bound


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr
        self.tree = SegmentTree(0, self.n)
        self.build(self.tree)

    def build(self, node: SegmentTree):
        if len(node) == 1:
            node.values = clc.Counter(self.arr[node.left_bound: node.right_bound])
            node.most_frequent = self.arr[node.left_bound]
            return
        node.split((node.left_bound + node.right_bound) // 2)
        self.build(node.left)
        self.build(node.right)
        node.values = node.left.values + node.right.values
        left_freq = node.left.most_frequent
        right_freq = node.right.most_frequent
        if (
            node.left.values[left_freq] + node.right.values[left_freq]
            >= node.left.values[right_freq] + node.right.values[right_freq]
        ):
            node.most_frequent = left_freq
        else:
            node.most_frequent = right_freq

    def query(self, left: int, right: int, threshold: int) -> int:
        counts_set, most_freqs = self.rec_query(self.tree, left, right + 1)
        for num in most_freqs:
            if sum(counts[num] for counts in counts_set) >= threshold:
                return num
        return -1

    def rec_query(self, node: int, left: int, right: int):
        if node.left_bound == left and node.right_bound == right:
            return [node.values], [node.most_frequent]
        if right <= node.mid:
            return self.rec_query(node.left, left, right)
        if left >= node.mid:
            return self.rec_query(node.right, left, right)
        left_values, left_set = self.rec_query(node.left, left, node.mid)
        right_values, right_set = self.rec_query(node.right, node.mid, right)
        return left_values + right_values, left_set + right_set
