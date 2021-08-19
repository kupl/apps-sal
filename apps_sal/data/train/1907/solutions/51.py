class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = [(original, cloned)]
        while q:
            (node_orig, node_clone) = q.pop()
            if node_orig is target:
                return node_clone
            if node_orig.left is not None:
                q.append((node_orig.left, node_clone.left))
            if node_orig.right is not None:
                q.append((node_orig.right, node_clone.right))
