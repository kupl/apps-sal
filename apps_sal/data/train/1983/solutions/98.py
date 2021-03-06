from collections import deque


class ProductOfNumbers:

    def __init__(self):
        self._stack = []

    def add(self, num: int) -> None:
        if num == 0:
            self._stack = []
        elif not self._stack:
            self._stack = [num]
        else:
            self._stack.append(self._stack[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > (n := len(self._stack)):
            return 0
        elif k == n:
            return self._stack[-1]
        else:
            return self._stack[-1] // self._stack[n - k - 1]
