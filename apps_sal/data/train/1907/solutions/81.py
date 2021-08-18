
class Solution:
    def getTargetCopy1(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node, lst):
            if node:
                lst.append(node)
                dfs(node.left, lst)
                dfs(node.right, lst)

        original_stack, cloned_stack = [], []
        dfs(original, original_stack)
        dfs(cloned, cloned_stack)

        for l1, l2 in zip(original_stack, cloned_stack):
            if l1 == target:
                return l2

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def it(node):
            if node:
                yield node
                yield from it(node.left)
                yield from it(node.right)

        for n1, n2 in zip(it(original), it(cloned)):
            if n1 == target:
                return n2
