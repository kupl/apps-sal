from collections import deque


class Solution:

    def bfs_helper(self, root):
        deep_sum = 0
        depth = 0
        queue = deque()
        queue.append([root, 0])
        while queue:
            (node, curr_depth) = queue.popleft()
            if not node.left and (not node.right):
                if depth < curr_depth:
                    deep_sum = node.val
                    depth = curr_depth
                else:
                    deep_sum += node.val
            else:
                if node.left:
                    queue.append([node.left, curr_depth + 1])
                if node.right:
                    queue.append([node.right, curr_depth + 1])
        return deep_sum

    def dfs_helper(self, root):
        deep_sum = 0
        depth = 0
        stack = list()
        stack.append([root, 0])
        while stack:
            (node, curr_depth) = stack.pop()
            if not node.left and (not node.right):
                if depth < curr_depth:
                    deep_sum = node.val
                    depth = curr_depth
                elif depth == curr_depth:
                    deep_sum += node.val
            else:
                if node.left:
                    stack.append([node.left, curr_depth + 1])
                if node.right:
                    stack.append([node.right, curr_depth + 1])
        return deep_sum

    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self.dfs_helper(root)
