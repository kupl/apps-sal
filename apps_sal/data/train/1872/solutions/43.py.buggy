# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        
        def recurse(root, level):
            if root:
                recurse(root.left, level+1)
                print(level)
                print(\"val\", root.val)
                level_store[level] +=root.val
                recurse(root.right, level+1)
        
        level_store = collections.defaultdict(int)
        recurse(root, level)
        
        print(level_store)
        max_so_far = float(\"-inf\")
        index = -1
        for key, value in level_store.items():
            if value>max_so_far:
                max_so_far = value
                index = key
            elif value==max_so_far:
                index=min(key, index)
                
        return index
                
                

