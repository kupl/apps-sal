class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.search(root)
        return root.min

    def search(self, node):
        if node.left:
            self.search(node.left)
            if node.right:
                self.search(node.right)
                node.min_with = 1 + node.left.min_bottom + node.right.min_bottom
                node.min_bottom = min(node.min_with, node.left.min + node.right.min)
                node.min = min(node.min_with, node.left.min_with + node.right.min,
                               node.left.min + node.right.min_with)
            else:
                node.min_bottom = node.left.min
                node.min_with = 1 + node.left.min_bottom
                node.min = min(node.min_with, node.left.min_with)
        else:
            if node.right:
                self.search(node.right)
                node.min_bottom = node.right.min
                node.min_with = 1 + node.right.min_bottom
                node.min = min(node.min_with, node.right.min_with)
            else:
                node.min_bottom = 0
                node.min_with = 1
                node.min = 1
