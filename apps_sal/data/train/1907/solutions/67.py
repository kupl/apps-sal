from collections import deque


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([(original, cloned)])
        while q:
            (node, cloned) = q.popleft()
            if node == target:
                return cloned
            if node.left:
                q.append((node.left, cloned.left))
            if node.right:
                q.append((node.right, cloned.right))
        return None
