class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        bfs = []
        level_sum = 0
        level_nodes = 1
        sum_of_levels = []
        while queue:
            node = queue.popleft()
            bfs.append(node)
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level_nodes -= 1
            if level_nodes == 0:
                sum_of_levels.append(level_sum)
                level_sum = 0
                level_nodes = len(queue)
        return sum_of_levels.index(max(sum_of_levels)) + 1
