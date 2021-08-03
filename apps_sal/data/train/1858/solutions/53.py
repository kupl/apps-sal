# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:

    def __init__(self, root: TreeNode):
        self.m = []

        q = [root]
        root.val = 0
        while q:
            node = q.pop()
            if node.left:
                node.left.val = 2 * node.val + 1
                self.m.append(node.left.val)
                q.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                q.append(node.right)
                self.m.append(node.right.val)

    def find(self, target: int) -> bool:
        return target in self.m


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
