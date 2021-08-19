# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned:
            return None

        S = [original]
        _S = [cloned]

        while len(S) > 0:
            curr = S.pop()
            _curr = _S.pop()

            if curr == target:
                return _curr

            if curr.left:
                S.append(curr.left)
                _S.append(_curr.left)
            if curr.right:
                S.append(curr.right)
                _S.append(_curr.right)

        return None
