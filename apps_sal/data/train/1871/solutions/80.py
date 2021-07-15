# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # pairs = []
    abs_max = -99999
    
    def construct_all_pairs(self, subtree):
        if subtree is None:
            return []
        else:
            lp = self.construct_all_pairs(subtree.left)
            rp = self.construct_all_pairs(subtree.right)
            for l in lp:
                # self.pairs.append((subtree.val, l))
                if abs(subtree.val - l) > self.abs_max:
                    self.abs_max = abs(subtree.val - l)
            for r in rp:
                # self.pairs.append((subtree.val, r))
                if abs(subtree.val - r) > self.abs_max:
                    self.abs_max = abs(subtree.val - r)
            return [subtree.val] + lp + rp
        
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.construct_all_pairs(root)
        return self.abs_max
        # print(self.pairs)
        # return max(map(lambda x : abs(x[0]-x[1]) , self.pairs))

