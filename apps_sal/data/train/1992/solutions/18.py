import itertools


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        char_arr = list(characters)
        self.data = itertools.combinations(char_arr, combinationLength)
        self.count = len(list(itertools.combinations(char_arr, combinationLength)))

    def __next__(self) -> str:
        ans = ''.join(next(self.data, ''))
        self.count -= 1
        return ans

    def hasNext(self) -> bool:
        return self.count > 0
