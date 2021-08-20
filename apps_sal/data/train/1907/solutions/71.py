class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def traverse(node):
            if node:
                yield node
                yield from traverse(node.left)
                yield from traverse(node.right)
        for (n1, n2) in zip(traverse(original), traverse(cloned)):
            if n1 == target:
                return n2
