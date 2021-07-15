class ProductOfNumbers:

    
    # [3, 0, 0, 2, 5, 4]
    # [(3, 1, -1), (0, 3, 1), (0, 1, 2), (2,1,2), (5,2,2), (4,10,2)]
    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        if not self.nums:
            last_zero = -1 if num else 0
            self.nums.append([num, 1, last_zero])
            return
            
        (last_val, last_product, last_zero) = self.nums[-1]
        
        last_zero = last_zero if num else len(self.nums)
        last_product = last_product * last_val or 1
        
        self.nums.append([num, last_product, last_zero])
        
    def getProduct(self, k: int) -> int:
        right_ind = len(self.nums) - 1
        left_ind = right_ind - k + 1
        
        if left_ind < 0:
            left_ind = 0
            
        (right_val, right_product, right_last_zero) = self.nums[right_ind]            
        (left_val, left_product, left_last_zero) = self.nums[left_ind]     
        
        if right_last_zero < left_ind:
            return right_val * right_product // left_product
        return 0
        
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

