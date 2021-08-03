

class Skiplist:

    def __init__(self):
        self.data_set = defaultdict(int)
        pass

    def search(self, target: int) -> bool:
        if target in self.data_set:
            return True
        return False

    def add(self, num: int) -> None:
        self.data_set[num] += 1
        return

    def erase(self, num: int) -> bool:
        if num in self.data_set:
            self.data_set[num] -= 1
            if self.data_set[num] == 0:
                del self.data_set[num]
            return True
        return False
