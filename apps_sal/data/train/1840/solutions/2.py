# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # dequeu node : [curr_node, state, longestdistance]
        ans = 0
        q = deque([[root, 'A', 0]])
        while (len(q) != 0):
            top, state, dist = q[0]
            ans = max(ans, dist)
            q.popleft()
            if state == 'A':
                if top.left:
                    q.append([top.left, 'L', 1])
                if top.right:
                    q.append([top.right, 'R', 1])
            else:
                if state == 'L':
                    if top.left:
                        q.append([top.left, 'L', 1])
                    if top.right:
                        q.append([top.right, 'R', dist + 1])
                if state == 'R':
                    if top.left:
                        q.append([top.left, 'L', dist + 1])
                    if top.right:
                        q.append([top.right, 'R', 1])
        return ans
