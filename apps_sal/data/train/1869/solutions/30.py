# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:

        if not S:
            return

        ins = list(S)

        root = TreeNode(-1)
        current = None

        while ins:

            while ins and ins[0] == '-':

                # if right present
                if current.right:
                    current = current.right
                # if left present
                elif current.left:
                    current = current.left

                ch = ins.pop(0)

            # node val can be multiple digits
            node_val = ''
            while ins and ins[0] != '-':
                ch = ins.pop(0)
                node_val += ch

            # if root None yet
            if not root.left:
                root.left = TreeNode(node_val)

            else:
                # if left not present
                if not current.left:
                    current.left = TreeNode(node_val)
                else:
                    current.right = TreeNode(node_val)

            # reset current
            current = root

        return root.left
