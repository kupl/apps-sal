class Solution:

    def helper(self, node, prenode, ans):
        if not node:
            return
        self.res = max(self.res, ans)
        if node == prenode.left:
            self.helper(node.right, node, ans + 1)
            self.helper(node.left, node, 1)
        elif node == prenode.right:
            self.helper(node.left, node, ans + 1)
            self.helper(node.right, node, 1)

    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root.left, root, 1)
        self.helper(root.right, root, 1)
        return self.res
