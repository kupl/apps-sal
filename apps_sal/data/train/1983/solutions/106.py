class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
        else:
            self.nums.append(num * self.nums[-1])

    def getProduct(self, k: int) -> int:
        if k >= len(self.nums):
            return 0
        return self.nums[-1] // self.nums[-k - 1]


class SlidingWindow:
    def __init__(self, k: int):
        self.k = k
        self.q = deque()
        self.zero_cnt = 0

    def add(self, val: int) -> None:
        if val == 0:
            self.zero_cnt = self.k
            self.q.append(1)
        else:
            self.zero_cnt -= 1
            prev = self.q[-1] if self.q else 1
            self.q.append(prev * val)
            if len(self.q) > self.k:
                if self.zero_cnt <= 0:
                    self.q[-1] /= self.q[0]
                self.q.popleft()

    def getProduct(self) -> int:
        if self.zero_cnt > 0:
            return 0
        return self.q[-1]


window = SlidingWindow(3)
window.add(1)
window.add(2)
assert window.getProduct() == 2
window.add(3)
assert window.getProduct() == 6
window.add(4)
assert window.getProduct() == 24
window.add(5)
assert window.getProduct() == 60


window = SlidingWindow(3)
window.add(3)
window.add(0)
window.add(2)
window.add(5)
assert window.getProduct() == 0
window.add(4)
assert window.getProduct() == 40
