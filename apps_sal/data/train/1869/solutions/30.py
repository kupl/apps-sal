class Solution:

    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return
        ins = list(S)
        root = TreeNode(-1)
        current = None
        while ins:
            while ins and ins[0] == '-':
                if current.right:
                    current = current.right
                elif current.left:
                    current = current.left
                ch = ins.pop(0)
            node_val = ''
            while ins and ins[0] != '-':
                ch = ins.pop(0)
                node_val += ch
            if not root.left:
                root.left = TreeNode(node_val)
            elif not current.left:
                current.left = TreeNode(node_val)
            else:
                current.right = TreeNode(node_val)
            current = root
        return root.left
