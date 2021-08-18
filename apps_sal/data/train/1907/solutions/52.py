
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def it(node):
            if node:
                yield node
                yield from it(node.left)
                yield from it(node.right)

        for n1, n2 in zip(it(original), it(cloned)):
            if n1 == target:
                return n2
