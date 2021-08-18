class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = []

        n = len(characters)
        for bitmask in range((1 << n)):
            if bin(bitmask).count('1') == combinationLength:
                curr = []
                for j in range(n):
                    if bitmask & (1 << n - j - 1):
                        curr.append(characters[j])
                self.combs.append(''.join(curr))

    def __next__(self) -> str:
        return self.combs.pop()

    def hasNext(self) -> bool:
        return self.combs
