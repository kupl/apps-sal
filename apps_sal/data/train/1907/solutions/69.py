from queue import Queue


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned == None:
            return None
        if cloned.val == target.val:
            return cloned
        cloned.left = self.getTargetCopy(original, cloned.left, target)
        if cloned.left != None:
            return cloned.left
        cloned.right = self.getTargetCopy(original, cloned.right, target)
        if cloned.right != None:
            return cloned.right
        return None
