import collections
import heapq
import sys


class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        lSums = dict()
        q = collections.deque()
        level = 0
        q.append(root)
        while q:
            size = len(q)
            level += 1
            levelSum = 0
            for i in range(size):
                node = q.popleft()
                levelSum += node.val
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            lSums[level] = levelSum
        minLevel = sys.maxsize
        maxSum = -sys.maxsize
        for level in lSums:
            localSum = lSums[level]
            if maxSum < localSum:
                minLevel = level
                maxSum = localSum
        return minLevel
