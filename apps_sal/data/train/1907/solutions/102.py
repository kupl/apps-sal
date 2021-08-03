from queue import Queue


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = Queue(maxsize=0)
        q.put((original, cloned))
        while(q):
            original, cloned = q.get()
            if(original == target):
                return cloned
            if(original.left):
                q.put((original.left, cloned.left))
            if(original.right):
                q.put((original.right, cloned.right))
        return None
