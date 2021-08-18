
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        visited = set()
        node = self.dfs(visited, cloned, target)

        return node

    def dfs(self, visited, node: TreeNode, target: TreeNode):
        visited.add(node)

        if node.val == target.val:
            return node

        if node.left and node.left not in visited:
            left = self.dfs(visited, node.left, target)
            if left is not None:
                return left

        if node.right and node.right not in visited:
            right = self.dfs(visited, node.right, target)
            if right is not None:
                return right

        return None
