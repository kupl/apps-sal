def targetcopy(original, cloned, target):
    if(original is None):
        return
    if(original == target):
        return cloned
    x = targetcopy(original.left, cloned.left, target)
    if(x):
        return x
    return targetcopy(original.right, cloned.right, target)


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return targetcopy(original, cloned, target)
