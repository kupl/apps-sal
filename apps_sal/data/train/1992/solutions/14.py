class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.n = combinationLength
        self.inds = [i for i in range(combinationLength)]
        self.iMax = len(self.chars)
        self.gotNext = True

    def __next__(self) -> str:
        print((self.inds))
        ans = ''.join([self.chars[i] for i in self.inds])
        c = 1
        i = self.n - 1
        while i >= 0 and c == 1:
            if self.inds[i] == self.iMax - self.n + i:
                c = 1
            else:
                c = 0
            i -= 1
        if i == -1 and c == 1:
            self.gotNext = False
        else:
            self.inds[i + 1] += 1
            for j in range(i + 2, self.n):
                self.inds[j] = self.inds[j - 1] + 1

        return ans

    def hasNext(self) -> bool:
        return self.gotNext
