class Skiplist:

    def __init__(self):
        self.d = {}

    def search(self, target: int) -> bool:
        return bool(self.d.get(target, False))

    def add(self, num: int) -> None:
        self.d[num] = self.d.get(num, 0) + 1

    def erase(self, num: int) -> bool:
        result = self.search(num)
        if result:
            self.d[num] -= 1
        return result
