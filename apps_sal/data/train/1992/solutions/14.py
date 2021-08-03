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


#         for i in range(self.n-1, -1 ,-1):
#             self.inds[i] += c
#             if self.inds[i] == self.iMax-self.n+i+1:
#                 if i != 0:
#                     self.inds[i] = self.inds[i-1] + 2
#                     c = 1
#                 else:
#                     self.gotNext = False
#             else:
#                 c = 0
        return ans

    def hasNext(self) -> bool:
        return self.gotNext


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
