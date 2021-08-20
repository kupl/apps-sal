class Solution:

    def smallestFromLeaf(self, root: TreeNode) -> str:
        minStr = chr(ord('z') + 1)
        cList = []

        def dfs(root):
            nonlocal minStr
            nonlocal cList
            print(cList)
            cList.append(root.val)
            if not root.left and (not root.right):
                minStr = min(minStr, ''.join((string.ascii_lowercase[i] for i in cList[::-1])))
                cList.pop()
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            cList.pop()
        dfs(root)
        return minStr
