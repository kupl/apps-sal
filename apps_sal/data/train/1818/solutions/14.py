# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # string.ascii_lowercase
    def smallestFromLeaf(self, root: TreeNode) -> str:
        minStr = chr(ord('z') + 1)
        # print(minStr)
        cList = []

        def dfs(root):
            nonlocal minStr
            nonlocal cList
            print(cList)

            cList.append(root.val)
            if not root.left and not root.right:
                minStr = min(minStr, ''.join(string.ascii_lowercase[i] for i in cList[::-1]))
                cList.pop()
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            cList.pop()

        dfs(root)
        return minStr
