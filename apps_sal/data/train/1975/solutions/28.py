class CustomStack:

    def __init__(self, maxSize: int):
        self._max_size = maxSize
        self._len = 0
        self._stack = []

    def push(self, x: int) -> None:
        if self._len < self._max_size:
            self._stack.insert(0, x)
            self._len += 1

    def pop(self) -> int:
        if self._len > 0:
            self._len -= 1
            ret = self._stack.pop(0)
        else:
            ret = -1
        return ret

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < k and i < self._len:
            self._stack[self._len - i - 1] += val
            i += 1
