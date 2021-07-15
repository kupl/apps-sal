# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def recur(node):
            if not node:
                return (None,None,None)
            lmaxi, lmini, lres = recur(node.left)
            rmaxi, rmini, rres = recur(node.right)
            print(\"node.val\", node.val)
            print(\"lmaxi, lmini, lres\", lmaxi, lmini, lres)
            print(\" rmaxi, rmini, rres\", rmaxi, rmini, rres)
            curr = node.val
            cv = [lmaxi, lmini, rmaxi, rmini]
            res = [lres, rres]
            res = res + [abs(curr-val) for val in cv if val!=None]
            res = [val for val in res if val!=None]
            
            minr = [lmini, rmini, curr]
            maxr = [lmaxi, rmaxi, curr]
            minr = [val for val in minr if val!=None]
            maxr = [val for val in maxr if val!=None]
            
            mini = min(minr)
            maxi = max(maxr)
            print(\"res arr\", res)
            res = max([0] + res)
            print(\"node, maxi, mini, res\", node.val, maxi, mini, res)
            return (maxi, mini, res)
        _,_,res = recur(root)
        return res
