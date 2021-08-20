class Skiplist:

    def __init__(self):
        self.data = []

    def search(self, target: int) -> bool:
        return self.data and target <= self.data[-1] and (target == self.data[bisect.bisect_left(self.data, target)])

    def add(self, num: int) -> None:
        bisect.insort(self.data, num)

    def erase(self, num: int) -> bool:
        if not self.data or num > self.data[-1]:
            return False
        i = bisect.bisect_left(self.data, num)
        if self.data[i] != num:
            return False
        self.data = self.data[:i] + self.data[i + 1:]
        return True
