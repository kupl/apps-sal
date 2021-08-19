class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        new_roots = []

        def delete_nodes(node, parent_deleted):
            if not node:
                return False
            delete = False
            for value in to_delete:
                if value == node.val:
                    delete = True
            if parent_deleted and (not delete):
                new_roots.append(node)
            (left, right) = (delete_nodes(node.left, delete), delete_nodes(node.right, delete))
            if left:
                node.left = None
            if right:
                node.right = None
            return delete
        delete_nodes(root, True)
        return new_roots
