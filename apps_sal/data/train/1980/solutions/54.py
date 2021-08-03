class Skiplist:

    def __init__(self):
        self._skiplist = []

    def search(self, target: int) -> bool:
        return target in self._skiplist

    def add(self, num: int) -> None:
        start = 0
        end = len(self._skiplist)
        while start < end:
            mid = int((start + end) / 2)
            if self._skiplist[mid] < num:
                start = mid + 1
            else:
                end = mid
        self._skiplist.insert(start, num)

    def erase(self, num: int) -> bool:
        if self.search(num):
            self._skiplist.remove(num)
            return True
        else:
            return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
