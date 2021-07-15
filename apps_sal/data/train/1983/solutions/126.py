class ProductOfNumbers:

    def __init__(self):
        self.queue = [1]
        self.zeroes = []

    def add(self, num: int) -> None:
        prev = 1 if not self.queue or self.queue[-1]==0 else self.queue[-1]
        self.queue.append(prev*num)
        if num == 0: self.zeroes.append(len(self.queue)-1)

    def getProduct(self, k: int) -> int:
        p = max (0, len(self.queue)-k-1)
        for idx in self.zeroes:
            if p < idx < len(self.queue): 
                return 0
        #print(self.queue,self.queue[p])
        if self.queue[p] != 0:
            return self.queue[-1] // self.queue[p]
        return self.queue[-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

