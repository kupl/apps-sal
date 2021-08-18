class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        ind = len(preorder)
        for i, j in enumerate(preorder):
            if j > root.val:
                ind = i
                break
        root.left = self.bstFromPreorder(preorder[1:ind])
        root.right = self.bstFromPreorder(preorder[ind:])

        return root
