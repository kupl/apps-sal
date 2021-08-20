class CustomStack:

    def __init__(self, maxSize: int):
        self.maxsize = maxSize
        self.currentsize = 0
        self._list = []

    def push(self, x: int) -> None:
        if self.currentsize < self.maxsize:
            self._list.append(x)
            self.currentsize += 1

    def pop(self) -> int:
        if self.currentsize > 0:
            lastelem = self._list.pop(-1)
            self.currentsize -= 1
            return lastelem
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for idx in range(k):
            if idx < len(self._list):
                self._list[idx] += val
