class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.traverse(root, root.val)
        return self.ans

    def traverse(self, root, so_far):
        if root:
            if root.val >= so_far:
                self.ans += 1
                so_far = root.val
            self.traverse(root.left, so_far)
            self.traverse(root.right, so_far)
