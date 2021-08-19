class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        return self.helper(preorder, 0, len(preorder))

    def helper(self, preorder, start, end):
        if start >= end:
            return None
        split = start + 1
        root = TreeNode(preorder[start])
        while split < end and preorder[start] > preorder[split]:
            split += 1
        root.left = self.helper(preorder, start + 1, split)
        root.right = self.helper(preorder, split, end)
        return root
