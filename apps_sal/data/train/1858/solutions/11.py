# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def recover(self, node, x):
        if node is None: return
        node.val = x
        self.vals.add(node.val)
        self.recover(node.left, (2*node.val)+1)
        self.recover(node.right, (2*node.val)+2)

    def __init__(self, root: TreeNode):
        root.val = 0
        self.vals = set()
        self._root = root
        self.recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

