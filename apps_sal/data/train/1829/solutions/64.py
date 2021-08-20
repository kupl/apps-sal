class Solution:

    def __init__(self):
        self.total_count = 0

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, float('-inf'))

    def goodNodesHelper(self, root, max_so_far):
        if not root:
            return
        if max_so_far <= root.val:
            max_so_far = root.val
            self.total_count += 1
        self.goodNodesHelper(root.left, max_so_far)
        self.goodNodesHelper(root.right, max_so_far)
        return self.total_count
