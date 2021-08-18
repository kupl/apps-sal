
class Solution:
    def __init__(self):
        self.node = None

    def findtarget(self, org, clone, target):

        if not org or not clone:
            return None

        if org.val == target.val == clone.val:
            return clone
        return self.findtarget(org.left, clone.left, target) or self.findtarget(org.right, clone.right, target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        return self.findtarget(original, cloned, target)
