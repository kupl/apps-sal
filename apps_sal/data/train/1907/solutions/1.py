
class Solution:
    def getTargetCopy(self, r1: TreeNode, r2: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = 0
        self.flag = False

        def inorder(node, node2):
            if self.flag:
                return
            if not node:
                return node
            if node.val == target.val:
                self.ans = node2
                self.flag = True
                return node2
            inorder(node.left, node2.left)
            inorder(node.right, node2.right)
        inorder(r1, r2)
        return self.ans
