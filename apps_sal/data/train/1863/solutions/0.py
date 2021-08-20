from collections import deque


class Solution:

    def bfs(self, root, col_table):
        min_col = 0
        max_col = 0
        queue = deque([(root, 0, 0)])
        while queue:
            (node, col, row) = queue.popleft()
            col_value = col_table.get(col, [])
            col_value.append((row, node.val))
            col_table[col] = col_value
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))
        return (min_col, max_col)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        col_table = dict()
        (min_col, max_col) = self.bfs(root, col_table)
        res = []
        for col_idx in range(min_col, max_col + 1):
            col_res = []
            col = sorted(col_table[col_idx])
            for i in range(len(col)):
                col_res.append(col[i][1])
            res.append(col_res)
        return res
