# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        \"\"\"
        #对于每个节点root，需要维护三种类型的状态：
        1. 状态a: root必须放置摄像头的情况下，覆盖整棵树需要的摄像头数目
        2. 状态b: 覆盖整棵树需要的摄像头数目，无论root是否放置摄像头。
        3. 状态c: 覆盖两颗子树需要的摄像头数目，无论节点root本身是否被监控到。

        \"\"\"
        def dfs(root):
            if not root:
                return [float('inf'), 0, 0]
            
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc +1
            b = min(a, la+rb, ra+lb)
            c = min(a, lb+rb)
            return [a, b, c]
        a, b, c = dfs(root)
        return b
        
