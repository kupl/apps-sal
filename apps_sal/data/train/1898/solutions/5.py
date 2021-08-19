# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        roots = []

        def deleting(node, to_delete, roots):
            if node == None:
                return
            elif node.val in to_delete:
                if node.left != None:
                    roots.append(node.left)
                if node.right != None:
                    roots.append(node.right)

                try:
                    while True:
                        roots.remove(node)
                except:
                    pass

            if node.left != None and node.left.val in to_delete:
                deleting(node.left, to_delete, roots)
                node.left = None
            else:
                deleting(node.left, to_delete, roots)

            if node.right != None and node.right.val in to_delete:
                deleting(node.right, to_delete, roots)
                node.right = None
            else:
                deleting(node.right, to_delete, roots)

        deleting(root, to_delete, roots)
        if root.val not in to_delete:
            roots.append(root)

        return roots
