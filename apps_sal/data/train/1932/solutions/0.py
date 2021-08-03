# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def count(node):
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)
        xNode = [0, 0]

        def process(node):
            if node:
                if node.val == x:
                    xNode[0] = count(node.left)
                    xNode[1] = count(node.right)
                else:
                    process(node.left)
                    process(node.right)
            return

        process(root)
        player2 = max(xNode[0], xNode[1], n - (xNode[0] + xNode[1] + 1))  # the maximum nodes I can color
        return player2 > n // 2
