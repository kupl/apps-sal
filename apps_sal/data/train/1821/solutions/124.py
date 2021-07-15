class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
    def insert(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:        
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
            
def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)
            

class Solution:
    root = None
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 0:
            self.root = node(nums[0])
            for val in nums[1:]:
                self.root.insert(val)
                res = []
            res = []
            inorder(self.root, res)
            print(res)
            return res
