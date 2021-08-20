from queue import Queue


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = Queue()
        q.put(cloned)
        while q.qsize():
            node = q.get()
            if node.val == target.val:
                return node
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
