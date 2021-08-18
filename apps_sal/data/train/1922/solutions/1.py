class Solution:
    def minCameraCover(self, root):
        self._res = 0
        if self._dfs(root) == 0:
            self._res += 1
        return self._res

    def _dfs(self, node):
        if not node:
            return 1

        left = self._dfs(node.left)
        right = self._dfs(node.right)

        if left == 0 or right == 0:
            self._res += 1
            return 2
        elif left == 2 or right == 2:
            return 1
        else:
            return 0
