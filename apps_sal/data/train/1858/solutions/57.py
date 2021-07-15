# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    
    def __init__(self, root: TreeNode):
        self.root = root
        self.values = list()
        self.regen(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

    def regen(self, root, v):
        if root == None: return
        
        root.val = v
        self.values.append(v)
        
        self.regen(root.left, 2*v+1)
        self.regen(root.right, 2*v+2)
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

