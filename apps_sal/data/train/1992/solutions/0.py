class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.nextCombIt = combinations(characters, combinationLength)
        self.nextComb = next(self.nextCombIt, None)

    def __next__(self) -> str:
        nextComb = self.nextComb
        self.nextComb = next(self.nextCombIt, None)
        return ''.join(nextComb)

    def hasNext(self) -> bool:
        return self.nextComb is not None
