class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return None
        bfs_queue = [root]
        current_sum = 0
        max_level = 0
        level = 0
        while True:
            temp = []
            level += 1
            row_sum = 0
            while bfs_queue:
                popped = bfs_queue.pop()
                row_sum += popped.val
                if popped.left:
                    temp.append(popped.left)
                if popped.right:
                    temp.append(popped.right)
            if not temp:
                if row_sum > current_sum:
                    max_level = level
                    current_sum = row_sum
                break
            else:
                if row_sum > current_sum:
                    max_level = level
                    current_sum = row_sum
                bfs_queue = temp
        return max_level
