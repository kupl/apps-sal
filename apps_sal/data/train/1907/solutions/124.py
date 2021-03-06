def traversal(original, cloned, target):
    if original == None:
        return None
    if original == target:
        return cloned
    res = traversal(original.left, cloned.left, target)
    if res != None:
        return res
    res = traversal(original.right, cloned.right, target)
    if res != None:
        return res
    return None


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return traversal(original, cloned, target)
