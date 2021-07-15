from collections import deque
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        x=cloned
        def clone(original,cloned,target,x):
            if original:
                if original==target:
                    x=cloned
                    return x
                return clone(original.left,cloned.left,target,x) or clone(original.right,cloned.right,target,x)
        return clone(original,cloned,target,x)
