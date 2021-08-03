# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: TreeNode) -> int:

        def add(l, n):
            nl = l.copy()
            nl.append(n)
            return nl

        self.res = 0

        def traverse(node, path):

            if node is None:
                return

            if(node.val >= max(path)):
                self.res += 1

            traverse(node.left, add(path, node.val))
            traverse(node.right, add(path, node.val))

        traverse(root, [-float('inf')])
        return self.res
