# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 自己写的
    def longestZigZag(self, root: TreeNode) -> int:
        
        # return longest zigzig path of current node from right / left
        def dfs(node):
            if not node.left and not node.right:
                return (0, 0)
            left = right = 0
            if node.left:
                left = dfs(node.left)[1] + 1
            if node.right:
                right = dfs(node.right)[0] + 1
            # res.append(max(left, right))
            # res[0] = max(res[0], max(left, right))
            self.res = max(self.res, max(left, right))
            return (left, right)
        
        # 这样反而会让时间变长
        # res = [0]
        # res = []
        self.res = 0
        dfs(root)
        # return max(res) if res else 0
        # return res[0]
        return self.res
