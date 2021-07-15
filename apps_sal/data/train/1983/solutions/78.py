'''

3,0,2,5,4,    8

k=1, 4
k=2, 20
k=3,40
k=4,0
k=5,0

d:

'''
class ProductOfNumbers:

    def __init__(self):
        self.size = 0
        self.d = {}
        self.lastZero = -1
        

    def add(self, num: int) -> None:
        self.size += 1
        if self.size <= 1 or self.d[self.size - 1] == 0:
            self.d[self.size] = num
        else:
            self.d[self.size] = num * self.d[self.size - 1]
        
        if num == 0:
            self.lastZero = self.size

        

    def getProduct(self, k: int) -> int:

        if self.size - k < self.lastZero: 
            return 0
        if self.size - k <= 0 or self.d[self.size - k] == 0: 
            return self.d[self.size]
        return self.d[self.size] // self.d[self.size - k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

