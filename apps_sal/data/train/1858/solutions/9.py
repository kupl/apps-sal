# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def helper(self, root, level):
        if not root:
            return None
        if level == 0:
            root.val = 0
            self.mem.add(root.val)
        if root.left:
            root.left.val = root.val * 2 + 1
            root.left = self.helper(root.left, level + 1)
            self.mem.add(root.left.val)
        if root.right:
            root.right.val = root.val * 2 + 2
            root.right = self.helper(root.right, level + 1)
            self.mem.add(root.right.val)
        return root
    
    def __init__(self, root: TreeNode):
        self.mem = set()
        self.helper(root, 0)
        
        

    def find(self, target: int) -> bool:
        return target in self.mem


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

