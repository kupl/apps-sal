from collections import deque


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        dq = deque()
        dq.append((original, cloned))
        while len(dq) > 0:
            (o, c) = dq.popleft()
            if o == target:
                return c
            if o.left is not None:
                dq.append((o.left, c.left))
            if o.right is not None:
                dq.append((o.right, c.right))
        return False
