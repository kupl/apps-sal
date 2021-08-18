class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        output = []
        stack = [(0, root)]

        def stackChildren(level, node):
            if node.right:
                stack.append((level, node.right))
                if level > 0 and node.right.val in to_delete:
                    node.right = None
            if node.left:
                stack.append((level, node.left))
                if level > 0 and node.left.val in to_delete:
                    node.left = None

        while stack:
            level, node = stack.pop()
            if node.val in to_delete:
                stackChildren(0, node)
            else:
                if level == 0:
                    output.append(node)
                stackChildren(level + 1, node)

        return output
