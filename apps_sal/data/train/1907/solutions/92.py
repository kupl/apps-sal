from collections import deque


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        num = target.val
        q = deque([cloned])
        while(q):
            curr = q.popleft()
            if(curr.val == num):
                return curr
            if(curr.left):
                q.append(curr.left)
            if(curr.right):
                q.append(curr.right)
        return None
