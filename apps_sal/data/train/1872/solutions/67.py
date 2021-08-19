# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.q = collections.deque()
        self.sums = collections.defaultdict()

    def bfs(self, root, visited):
        self.q.append(root)
        idx = 1

        while self.q:
            level = len(self.q)
            self.sums[idx] = 0
            while level:
                p = self.q.popleft()

                if p is None or p in visited:
                    level -= 1
                    continue

                self.sums[idx] += p.val

                self.q.append(p.left)
                self.q.append(p.right)

                level -= 1

            idx += 1

    def maxLevelSum(self, root: TreeNode) -> int:
        visited = []
        self.bfs(root, visited)
        max_sum = level = 0

        for key, value in self.sums.items():
            if value > max_sum:
                max_sum = value
                level = key

        return level
