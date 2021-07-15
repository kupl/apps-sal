# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    
    def __init__(self, root: TreeNode):
        if not root:
            return root
        self.root = root
        self.root.val = 0
        self.vals = []
        self.vals.append(self.root.val)
        self.construct(self.root)
        print((self.vals))
        
        
    def construct(self, root):
        if root.left:
            root.left.val = 2*root.val + 1
            self.vals.append(root.left.val)
            self.construct(root.left)
        if root.right:
            root.right.val = 2*root.val + 2
            self.vals.append(root.right.val)
            self.construct(root.right)
        return root

    def find(self, target: int) -> bool:
        if target in self.vals:
            return True
        return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

