# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import collections

    def maxLevelSum(self, root: TreeNode) -> int:
        #         bfs to do level traversal and calculate sum, update level if sum is larger
        levelSum = float('-inf')
        res = 0
        queue = collections.deque()
        queue.append((1, root))
        while len(queue) != 0:
            curr_sum = 0
            for _ in range(len(queue)):
                currl, curr = queue.popleft()
                curr_sum += curr.val
                if curr.left:
                    queue.append((currl + 1, curr.left))
                if curr.right:
                    queue.append((currl + 1, curr.right))
            if curr_sum > levelSum:
                res = currl
                levelSum = curr_sum
        return res
