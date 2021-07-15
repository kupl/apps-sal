# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.ss = set()
        self.restoreTree(root, 0)
        
        
    def restoreTree(self, root: TreeNode, val: int):
        if not root: return
        else: 
            root.val = val
            self.ss.add(val)
        if root.left: self.restoreTree(root.left, 2 * val + 1)
        if root.right: self.restoreTree(root.right, 2 * val + 2)
        return

    def find(self, target: int) -> bool:
        return target in self.ss
    \"\"\"\"
        root = self.root
        if not root: return False
        if root.val == target: return True
        left, right = False, False
        if root.left: left = self.findItem(target, root.left)
        if root.right: right = self.findItem(target, root.right)
        return left or right
        


    def findItem(self, target: int, root: TreeNode):
        if not root: return False
        if root.val == target: return True
        left, right = False, False
        if root.left: left = self.findItem(target, root.left)
        if root.right: right = self.findItem(target, root.right)
        return left or right
        
\"\"\"
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
