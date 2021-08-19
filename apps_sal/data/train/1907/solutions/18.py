class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [original]
        cloned_q = [cloned]
        while True:
            curr = queue.pop(0)
            cloned_curr = cloned_q.pop(0)
            if curr == target:
                return cloned_curr
            if curr.left:
                queue.append(curr.left)
                cloned_q.append(cloned_curr.left)
            if curr.right:
                queue.append(curr.right)
                cloned_q.append(cloned_curr.right)
