
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([cloned])
        while q:
            p = q.popleft()
            if p.val == target.val:
                return p
            q += [c for c in [p.left, p.right] if c]
