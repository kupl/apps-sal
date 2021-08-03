# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def check(root):
            r = chr(root.val + 97)
            if root.left == None and root.right == None:
                return [r]

            r1 = []
            r2 = []
            if root.left != None:
                r1 = check(root.left)
            if root.right != None:
                r2 = check(root.right)
            rtv = []
            small = min(r1 + r2)
            #   前缀相同的，需要保留，因为未来可能翻盘
            for x in r1 + r2:
                if x.startswith(small):
                    rtv.append(x + r)
            rtv.insert(0, small + r)

            return rtv
            pass

        #   输入非空：The number of nodes in the given tree will be between 1 and 8500.
        rtv = check(root)
        return min(rtv)
