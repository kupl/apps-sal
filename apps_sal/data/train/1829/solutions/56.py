# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, path):

            if root:
                indx = bisect.bisect(path, root.val)
                if indx == len(path):
                    # res.append(root.val)
                    self.count += 1
                dfs(root.left, path[:indx] + [root.val] + path[indx:])
                dfs(root.right, path[:indx] + [root.val] + path[indx:])
        # res=[]
        self.count = 0
        dfs(root, [])
        # print(res)
        return self.count
