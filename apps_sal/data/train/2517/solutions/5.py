class Solution:
    trib = [0, 1, 1]

    def tribonacci(self, n: int) -> int:
        try:
            return self.trib[n]
        except:
            currlen = len(self.trib)
            for i in range(currlen, n + 1):
                self.trib.append(self.trib[i - 1] + self.trib[i - 2] + self.trib[i - 3])
            return self.trib[n]
