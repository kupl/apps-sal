# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        import collections
        queue = collections.deque([root])
        maxx = root.val
        ans = 0
        level = 1
        while queue:
            summ = 0
            for i in range(len(queue)):
                n = queue.popleft()
                if not n:
                    continue
                summ += n.val
                queue.append(n.left)
                queue.append(n.right)
            if summ > maxx:
                ans = level
                maxx = summ
            level += 1
        return ans
