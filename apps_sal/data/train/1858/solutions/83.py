# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):

        self.values = []

        def evaluate(node, value):

            if not node:
                return

            node.val = value

            self.values.append(value)

            evaluate(node.left, value * 2 + 1)
            evaluate(node.right, value * 2 + 2)

        evaluate(root, 0)

    def find(self, target: int) -> bool:

        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
