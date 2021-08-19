from itertools import combinations
from math import factorial


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.base = characters
        self.start = 0
        self.end = factorial(len(characters)) / factorial(combinationLength) / factorial(len(characters) - combinationLength)
        self.strBase = combinations(characters, combinationLength)

    def __next__(self) -> str:
        if self.hasNext():
            self.start += 1
            val = next(self.strBase)
            return ''.join(val)
        else:
            raise StopIteration

    def hasNext(self) -> bool:
        return self.start < self.end


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
