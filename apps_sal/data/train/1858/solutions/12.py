# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):

        self.vals = set()

        def build(root, x):
            root.val = x
            self.vals.add(x)
            if root.left:
                build(root.left, 2 * x + 1)
            if root.right:
                build(root.right, 2 * x + 2)

        build(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
