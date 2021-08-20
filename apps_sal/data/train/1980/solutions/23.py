class Skiplist:

    def __init__(self):
        self.skip_list = {}

    def search(self, target: int) -> bool:
        if target in self.skip_list:
            if self.skip_list[target] > 0:
                return True
        return False

    def add(self, num: int) -> None:
        if num in self.skip_list:
            self.skip_list[num] += 1
        else:
            self.skip_list[num] = 1

    def erase(self, num: int) -> bool:
        if num in self.skip_list:
            if self.skip_list[num] > 0:
                self.skip_list[num] -= 1
                return True
        return False
