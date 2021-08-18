class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.N = combinationLength
        self.cl = len(characters)
        self.sym = characters
        self.precom = self.__pre(self.cl, combinationLength)
        self.index = len(self.precom) - 1

    def __next__(self) -> str:
        curr = self.precom[self.index]
        res = []
        for i, c in enumerate(curr):
            if c == '1':
                res.append(self.sym[i])
        self.index -= 1
        return ''.join(res)

    def hasNext(self) -> bool:
        if self.index < 0:
            return False
        return True

    def __pre(self, N, M):
        maxi = 2**N
        res = []
        for curr in range(maxi):
            binary = bin(curr)[2:]
            if binary.count('1') == M:
                res.append(binary.zfill(N))
        return res
