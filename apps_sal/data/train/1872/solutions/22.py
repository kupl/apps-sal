from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque([[root, 1]])
        best = -math.inf
        ans = 1
        last = 1
        total = 0

        while queue:
            node = queue.popleft()
            if last != node[1]:
                if total > best:
                    best = total
                    ans = last
                last = node[1]
                total = 0

            if not node[0]:
                continue

            total += node[0].val

            lvl = node[1] + 1
            queue.append([node[0].left, lvl])
            queue.append([node[0].right, lvl])

        return ans
