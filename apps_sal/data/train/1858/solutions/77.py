# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):

        self.arr = []

        def convert(curr):
            if curr:
                x = curr.val

                self.arr.append(x)
                if curr.left:
                    curr.left.val = 2 * x + 1
                if curr.right:
                    curr.right.val = 2 * x + 2

                convert(curr.left)
                convert(curr.right)

        root.val = 0
        convert(root)

    def find(self, target: int) -> bool:

        return target in self.arr


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
