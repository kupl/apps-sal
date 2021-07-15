# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        def traverse(node: TreeNode, layer: int, nums: List[int]):
            if node is None:
                return
            
            while len(nums) < layer+1:
                nums.append([])
            nums[layer].append(node.val)
            
            traverse(node.left,layer+1,nums)
            traverse(node.right,layer+1,nums)
        
        by_layer = []
        
        traverse(root,0,by_layer)
        # print(by_layer)
        return sum(by_layer[-1])
