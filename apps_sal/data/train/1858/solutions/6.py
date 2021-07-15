# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        values = set()
        def recover(head, val):
            if head is None:
                return
            head.val = val
            values.add(val)
            recover(head.left, val * 2 + 1)
            recover(head.right, val * 2 + 2)
        recover(root, 0)
        self.values = values

    def find(self, target: int) -> bool:
        return target in self.values
            

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

