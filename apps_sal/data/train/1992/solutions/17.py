class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.k = combinationLength
        self.r = []
        self.dfs('', 0)

    def dfs(self, st, idx):
        if len(st) == self.k:
            self.r.append(st)
            return
        for i in range(idx, len(self.s)):
            self.dfs(st + self.s[i], i + 1)

    def __next__(self) -> str:
        return self.r.pop(0)

    def hasNext(self) -> bool:
        return len(self.r) != 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
