class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.comb = list(map(lambda x: \"\".join(x), list(itertools.combinations(characters,combinationLength))))[::-1]


    def next(self) -> str:
        return self.comb.pop()

    def hasNext(self) -> bool:
        return (len(self.comb) != 0)      


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
