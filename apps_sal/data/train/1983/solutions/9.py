import bisect 
class ProductOfNumbers:

    def __init__(self):
        self.time = 0
        self.d = collections.defaultdict(list)

    def add(self, num: int) -> None:
        self.time += 1
        self.d[num].append((self.time, len(self.d[num])))

    def getProduct(self, k: int) -> int:
        res = 1
        for num in range(101):
            i = bisect.bisect_right(self.d[num], (self.time-k+1,-1), )
            res *= num**(len(self.d[num]) - i)
        return res

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

