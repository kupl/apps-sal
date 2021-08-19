# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root == None:
            return None

        canRootLeft = self.validSubtree(root.left, limit, root.val)
        canRootRight = self.validSubtree(root.right, limit, root.val)

        root.left = (root.left if canRootLeft else None)
        root.right = (root.right if canRootRight else None)

        if not canRootLeft and not canRootRight:
            return None
        else:
            return root

    def validSubtree(self, node: TreeNode, limit: int, currentVal: int) -> bool:
        # Handling base-case leafs
        if node == None:
            return (currentVal >= limit)

        canLeft = self.validSubtree(node.left, limit, node.val + currentVal)
        canRight = self.validSubtree(node.right, limit, node.val + currentVal)

        # Handling single-branch values
        if (node.left and not node.right):
            # Using our node left value
            canRight = canLeft
        elif (node.right and not node.left):
            canLeft = canRight

        node.left = (node.left if canLeft else None)
        node.right = (node.right if canRight else None)

        if not canLeft and not canRight:
            return False
        else:
            return canLeft or canRight
