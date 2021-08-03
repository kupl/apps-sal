# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        root.val = 0
        self.nodes = []

        self.recoverTree(root, 0)

    def recoverTree(self, root, x):
        current = root

        if current:
            print((current.val, x))
            if current.val == x:
                self.nodes.append(current.val)
                if current.left:
                    current.left.val = 2 * x + 1
                    self.recoverTree(current.left, current.left.val)

                if current.right:
                    current.right.val = 2 * x + 2
                    self.recoverTree(current.right, current.right.val)

    def find(self, target: int) -> bool:
        if target in self.nodes:
            return True

        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
