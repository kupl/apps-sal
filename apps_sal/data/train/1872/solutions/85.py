from collections import deque


class Node:

    def __init__(self, treeNode, level):
        self.treeNode = treeNode
        self.level = level


class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque([Node(root, 1)])
        level = 1
        total = 0
        totalMax = 0
        ans = 1
        while queue:
            cur = queue.popleft()
            if cur.level != level:
                if total > totalMax:
                    totalMax = total
                    ans = level
                level = cur.level
                total = 0
            total += cur.treeNode.val
            if cur.treeNode.left:
                queue.append(Node(cur.treeNode.left, cur.level + 1))
            if cur.treeNode.right:
                queue.append(Node(cur.treeNode.right, cur.level + 1))
        return ans
