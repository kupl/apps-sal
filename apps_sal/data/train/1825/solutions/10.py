# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        node0, node1 = None, None
        q = [root]
        while q:
            node0, node1 = q[0], q[-1]
            q = [child for node in q for child in (node.left, node.right) if child]
        if node0 == node1:
            return node0
        result = None
        # NodeWithStatus = collections.namedtuple('NodeWithStatus', ['node','status'])

        def lca(root: TreeNode) -> bool:
            nonlocal result
            if root is None:
                return False
            left = lca(root.left)
            right = lca(root.right)
            if left and right:
                result = root
            return (root == node0 or root == node1) or left or right
        lca(root)
        return result
