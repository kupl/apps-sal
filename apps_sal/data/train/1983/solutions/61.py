from functools import reduce
class ProductOfNumbers:

    def __init__(self):
        self.list = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.list = [1]
        else:
            result = self.list[-1]*num
            self.list.append(result)

    def getProduct2(self, k: int) -> int:
        return reduce(lambda x,y:  x*y, self.list[-k:])
    
    def getProduct(self, k: int) -> int:
        if len(self.list) <= k:
            return 0
        
        ind = -1 - k 
        if self.list[ind] == 0:
            return 0
        else:
            return self.list[-1]//self.list[ind]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


#[3,0,2,2,5,4]
#[3, 0, 1, 2,  4, 20, 80]
#last 2 list[-1]/list[(-2-1)] => 80/4 = 20  
#last 3  => 80/2 = 40
#last 4 => 80/ 1 = 80
# last 5 => list[-6] == 0 => 0
# last 6 => 0 

# [2,3,4,5,6]
# l = 5 
# [2, 6, 24, 120, 720]
# last 2 => 30
# last 3 => 720/6 = 120 
# last 4 => 720/2 = 360 
# last 5 => list[-1]

