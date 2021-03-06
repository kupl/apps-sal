class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.num_to_index = collections.defaultdict(list)
        for x in range(len(arr)):
            self.num_to_index[arr[x]].append(x)
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        visited = set()
        length = right - left + 1
        for x in range(left, right + 1):
            if self.arr[x] in visited:
                continue
            left_i = bisect.bisect_left(self.num_to_index[self.arr[x]], left)
            right_i = bisect.bisect_right(self.num_to_index[self.arr[x]], right) - 1
            if right_i - left_i + 1 >= threshold:
                return self.arr[x]
            length = length - (right_i - left_i + 1)
            if threshold > length:
                return -1
            visited.add(self.arr[x])
        return -1
