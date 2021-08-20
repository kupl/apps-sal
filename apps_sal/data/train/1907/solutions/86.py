class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.recur(cloned, target)

    def recur(self, node, target):
        if node.val == target.val:
            return node
        (a, b) = (None, None)
        if node.left:
            a = self.recur(node.left, target)
        if node.right:
            b = self.recur(node.right, target)
        return a or b
