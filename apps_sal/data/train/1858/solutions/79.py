# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.data = set()

        def walk(node, v):
            if(not node):
                return

            self.data.add(v)
            walk(node.left, 2 * v + 1)
            walk(node.right, 2 * v + 2)

        walk(root, 0)

    def find(self, target: int) -> bool:
        return target in self.data


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
