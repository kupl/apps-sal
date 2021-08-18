
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.search(cloned, target)

    def search(self, node, target):
        if node == None:
            return None
        if node.val == target.val:
            return node
        n = self.search(node.left, target)
        if n:
            return n
        n = self.search(node.right, target)
        return n
