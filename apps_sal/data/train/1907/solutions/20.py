from collections import deque


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque()
        q.append(cloned)
        while len(q):
            current = q.popleft()
            if current.val == target.val:
                return current
            q.extend([child for child in [current.left, current.right] if child is not None])
