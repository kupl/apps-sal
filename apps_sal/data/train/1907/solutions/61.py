class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def it(root: TreeNode) -> TreeNode:
            if root:
                yield root
                yield from it(root.left)
                yield from it(root.right)
        for (t1, t2) in zip(it(original), it(cloned)):
            if t1 == target:
                return t2
