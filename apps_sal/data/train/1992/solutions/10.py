def rec(s, l, arr, current):
    for i in range(len(s)):
        current.append(s[i])
        if len(current) == l:
            arr.append(''.join(current))
        rec(s[i + 1:], l, arr, current)
        current.pop(len(current) - 1)


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.index = 0
        self.arr = []
        c = []
        rec(characters, combinationLength, self.arr, c)

    def __next__(self) -> str:
        ret = self.arr[self.index]
        self.index += 1
        return ret

    def hasNext(self) -> bool:
        if self.index < len(self.arr):
            return True
        return False
