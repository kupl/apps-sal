# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        self.arr = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)
        def solve(nums):
            if len(nums):
                #print(nums)
                mx = nums.index(max(nums))
                root  = TreeNode(nums[mx])
                root.left = solve(nums[:mx])
                root.right = solve(nums[mx+1:])
                return root
        
    
        inorder(root)
        self.arr.append(val)
        return solve(self.arr)
        

