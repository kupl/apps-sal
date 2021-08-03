class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def dfs(start, path):
            if len(path) == self.combinationLength:
                yield ''.join(path)
            else:
                for i in range(start, len(self.characters)):
                    path.append(self.characters[i])
                    yield from dfs(i + 1, path)
                    path.pop()

        self.characters = sorted(characters)
        self.combinationLength = combinationLength
        self.next_val = None
        self.comb = dfs(0, [])

    def __next__(self) -> str:
        if self.next_val:
            tmp = self.next_val
            self.next_val = None
            return tmp
        else:
            return next(self.comb)

    def hasNext(self) -> bool:
        if self.next_val:
            return True
        else:
            self.next_val = next(self.comb, False)
            return bool(self.next_val)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
