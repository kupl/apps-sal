class Solution:

    def __init__(self):
        self.node = None

    def findtarget(self, org, clone, target):
        if not org or not clone:
            return
        if org.val == target.val == clone.val:
            self.node = clone
            return
        self.findtarget(org.left, clone.left, target)
        self.findtarget(org.right, clone.right, target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.findtarget(original, cloned, target)
        return self.node
