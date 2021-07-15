# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.allval = self._fix(root, 0)

    def find(self, target: int) -> bool:
        return target in self.allval
    
    def _fix(self, node, root_val):
        if node is None:
            return []
        
        node.val = root_val
        lv = self._fix(node.left, 2*root_val+1)
        rv = self._fix(node.right, 2*root_val+2)
        
        return [root_val] + lv + rv
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

