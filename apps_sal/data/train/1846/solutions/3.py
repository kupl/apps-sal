class Solution:

    def pruneTree(self, root: TreeNode) -> TreeNode:

        def check(node):
            if not node.left:
                l = True
            else:
                l = check(node.left)
            if not node.right:
                r = True
            else:
                r = check(node.right)
            if l:
                node.left = None
            if r:
                node.right = None
            return l and r and (node.val == 0)
        ans = TreeNode()
        ans.right = root
        check(ans)
        return ans.right
