class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        final_list = []

        def rec(node):
            if node == None:
                return None
            node.left = rec(node.left)
            node.right = rec(node.right)
            if node.val in to_delete:
                if node.left != None:
                    final_list.append(node.left)
                if node.right != None:
                    final_list.append(node.right)
                return None
            return node
        rec(root)
        if root.val not in to_delete:
            final_list.append(root)
        return final_list
