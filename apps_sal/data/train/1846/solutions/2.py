class Solution:

    def pruneTree(self, root: TreeNode) -> TreeNode:

        def prune(node: TreeNode) -> bool:
            if not node:
                return True
            left_prune = prune(node.left)
            right_prune = prune(node.right)
            if prune(node.left):
                node.left = None
            if prune(node.right):
                node.right = None
            return node.val == 0 and left_prune and right_prune
        if prune(root):
            return None
        return root
