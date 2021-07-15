class ProductOfNumbers:

    def __init__(self):
        self.c=[1 for i in range(40000)]
        self.size=0
        self.z=-1
        
    def add(self, num: int) -> None:
        if(num==0):
            num=1
            self.z=self.size
        if(self.size==0):
            self.c[0]=num
            self.size+=1
            return
        self.c[self.size]*=self.c[self.size-1]*num
        self.size+=1

    def getProduct(self, k: int) -> int:
        if(self.size-self.z<=k):
            return 0
        return self.c[self.size-1]//self.c[self.size-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

