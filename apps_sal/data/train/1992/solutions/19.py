class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chs = characters
        self.comblen = combinationLength
        self.totlen = len(self.chs)
        self.idx = [_ for _ in range(self.comblen)]
        self.idx[-1] -= 1

    def __next__(self) -> str:
        k = self.comblen
        while k > 0:
            k -= 1
            self.idx[k] += 1
            if self.idx[k] < self.totlen + k + 1 - self.comblen:
                break
        for i in range(k + 1, self.comblen):
            self.idx[i] = self.idx[i - 1] + 1

        return ''.join([self.chs[k] for k in self.idx])

    def hasNext(self) -> bool:
        return self.idx[0] != self.totlen - self.comblen
