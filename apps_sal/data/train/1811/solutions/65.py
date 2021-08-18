class StockSpanner:

    def __init__(self):
        self.nums = []
        self.larger_pos = []

    def next(self, price: int) -> int:
        if not self.nums:
            self.nums.append(price)
            self.larger_pos.append(-1)
            return 1
        num = self.nums[-1]
        pos = len(self.larger_pos) - 1
        while price >= num:
            pos = self.larger_pos[pos]
            if pos == -1:
                self.nums.append(price)
                self.larger_pos.append(-1)
                return len(self.nums)
            num = self.nums[pos]
        self.nums.append(price)
        self.larger_pos.append(pos)
        return len(self.nums) - 1 - pos
