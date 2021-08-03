# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def recoverTree(self, node: TreeNode) -> None:
        if not node.left and not node.right:
            return None
        if node.left:
            node.left.val = 2 * node.val + 1
            self.num_set.add(node.left.val)
            self.recoverTree(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self.num_set.add(node.right.val)
            self.recoverTree(node.right)

    def __init__(self, root: TreeNode):
        root.val = 0
        self.num_set = set()
        self.num_set.add(0)
        self.recoverTree(root)
        self.root = root

    def find(self, target: int) -> bool:
        if target < self.root.val:
            return False
        return target in self.num_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
