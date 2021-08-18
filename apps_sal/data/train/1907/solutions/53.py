
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def lis(root):
            if root:
                yield root
                yield from lis(root.left)
                yield from lis(root.right)

        for a, b in zip(lis(original), lis(cloned)):
            if a == target:
                return b
