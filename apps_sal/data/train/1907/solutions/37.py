
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = [(original, cloned)]
        while q:
            a, b = q.pop()
            if a.val == target.val:
                return b
            else:
                if a.left is not None:
                    q.append((a.left, b.left))
                if a.right is not None:
                    q.append((a.right, b.right))
