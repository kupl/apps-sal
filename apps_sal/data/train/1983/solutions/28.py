class ProductOfNumbers:

    def __init__(self):
        self.mylist=[]
        

    def add(self, num: int) -> None:
        self.mylist.append(num)
        # print(self.mylist)

    def getProduct(self, k: int) -> int:
        this_list=self.mylist[-k:]
        # print(k,this_list,math.prod(this_list) )
        return math.prod(this_list) 


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

