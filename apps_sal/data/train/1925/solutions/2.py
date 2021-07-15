class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and stack[-1].val < val:
                    last = stack.pop()
                last.right = node
            stack.append(node)
        return root
