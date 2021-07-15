class ProductOfNumbers:

    def __init__(self):
        self.l = list()
        self.last_zero = 0
        self.start_ones = 0
        
    def add(self, num: int) -> None:
        
        if num == 1:
            self.start_ones +=1
        else:
            self.start_ones = 0
        self.l.insert(0,num)
        
        if num == 0:
            self.last_zero = 0
        else:
            self.last_zero += 1

    def getProduct(self, k: int) -> int:
        
        
        if self.last_zero and self.last_zero < k:
            return 0
        
        if self.start_ones > k:
            return 1
        
        r = k
        if self.start_ones > 0:
            r -= self.start_ones - 1
        
        prod = 1
        idx = 0
        #print(self.start_ones,k)
        for idx in range(r):
            #print('->',self.l[idx])
            prod *= self.l[idx] if idx < len(self.l) else 1
        return prod

\"\"\"
[\"ProductOfNumbers\",\"add\",\"getProduct\",\"getProduct\",\"add\",\"getProduct\",\"add\",\"add\",\"add\",\"getProduct\",\"getProduct\",\"getProduct\",\"add\",\"add\",\"add\"]
[[],[1],[1],[1],[59],[2],[59],[34],[95],[1],[1],[1],[64],[0],[11]]
[null,null,1,1,null,59,null,null,null,95,95,95,null,null,null]
\"\"\"    
    
# [\"ProductOfNumbers\",\"add\",\"add\",\"add\",\"add\",\"add\",\"add\",\"add\",\"add\",\"getProduct\",\"getProduct\",\"getProduct\",\"getProduct\",\"add\"]
# [[],[2],[4],[1],[7],[4],[1],[4],[2],[3],[5],[6],[8],[4]]
# [null,null,null,null,null,null,null,null,null,8,224,224,1792,null]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
