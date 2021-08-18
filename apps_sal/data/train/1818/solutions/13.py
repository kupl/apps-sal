class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root is None:
            return ''

        stack = [[root]]
        min_string = 'z' * 9999

        while stack:
            current = stack.pop()
            if current[-1].left is None and current[-1].right is None:
                min_string = min(min_string, ''.join(chr(65 + i.val).lower() for i in reversed(current)))

            if current[-1].left:
                stack.append(current + [current[-1].left])
            if current[-1].right:
                stack.append(current + [current[-1].right])
        return min_string
