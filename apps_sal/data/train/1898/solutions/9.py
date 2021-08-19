class Solution:

    def walk(self, node, to_delete):
        if not node:
            return []
        roots = []
        if node.left:
            roots += self.walk(node.left, to_delete)
            if node.left.val in to_delete:
                node.left = None
            elif node.val in to_delete:
                roots.append(node.left)
        if node.right:
            roots += self.walk(node.right, to_delete)
            if node.right.val in to_delete:
                node.right = None
            elif node.val in to_delete:
                roots.append(node.right)
        return roots

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return None
        to_delete = set(to_delete)
        roots = self.walk(root, to_delete)
        if root.val not in to_delete:
            roots.append(root)
        return roots
