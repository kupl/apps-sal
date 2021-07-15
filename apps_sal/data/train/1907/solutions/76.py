# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        p=[]
        ok=0
        def dfs(i):
            if not i:
                return
            nonlocal ok
            if i==target:
                ok=1
                return
            p.append(0)
            dfs(i.left)
            if ok:
                return
            else:
                p.pop()
            p.append(1)
            dfs(i.right)
            if ok:
                return
            else:
                p.pop()
        dfs(original)
        i=cloned
        for x in p:
            if x==0:
                i=i.left
            else:
                i=i.right
        return i
