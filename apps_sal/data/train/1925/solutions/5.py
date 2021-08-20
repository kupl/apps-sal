class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder or len(preorder) == 0:
            return None
        inorder = sorted(preorder)
        root = TreeNode(preorder[0])
        leftLen = inorder.index(root.val)
        root.left = self.bstFromPreorder(preorder[1:1 + leftLen])
        root.right = self.bstFromPreorder(preorder[1 + leftLen:])
        return root
