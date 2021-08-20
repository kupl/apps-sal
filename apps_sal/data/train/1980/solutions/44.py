class Skiplist:

    def __init__(self):
        self.nums = []

    def search(self, target: int) -> bool:
        if not self.nums:
            return False
        idx = bisect.bisect_left(self.nums, target)
        if idx < len(self.nums) and self.nums[idx] == target:
            return True
        return False

    def add(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def erase(self, num: int) -> bool:
        if not self.search(num):
            return False
        idx = bisect.bisect_left(self.nums, num)
        self.nums.pop(idx)
        return True
