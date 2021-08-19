class Solution:

    def __init__(self):
        self.max_depth = 0
        self.ancestor = None

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.dfs(root, 0)
        return self.ancestor

    def dfs(self, node: TreeNode, curr_depth) -> int:
        (curr_deepest_L, curr_deepest_R) = (curr_depth, curr_depth)
        if not node.left and (not node.right):
            if curr_depth > self.max_depth:
                self.max_depth = curr_depth
                self.ancestor = node
            return curr_depth
        if node.left:
            curr_deepest_L = self.dfs(node.left, curr_depth + 1)
        if node.right:
            curr_deepest_R = self.dfs(node.right, curr_depth + 1)
        if curr_deepest_L == curr_deepest_R == self.max_depth:
            self.ancestor = node
        return max(curr_deepest_L, curr_deepest_R)
