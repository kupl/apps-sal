# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def targetcopy(original, cloned, target):
    if(original is None):
        return
    # print(original.val,cloned.val,target.val)
    if(original == target):
        return cloned
    x = targetcopy(original.left, cloned.left, target)
    if(x):
        return x
    return targetcopy(original.right, cloned.right, target)


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return targetcopy(original, cloned, target)
