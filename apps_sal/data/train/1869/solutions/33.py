class Solution:

    def recoverFromPreorder(self, S: str) -> TreeNode:
        try:
            self.values = [int(i) for i in S.split('-') if len(i) > 0]
            self.S = S[S.index('-'):]
            root = TreeNode(self.values.pop(0))
        except:
            return TreeNode(int(S))

        def create_tree(root, depth):
            if len(self.S) == 0:
                return
            elif '-' * depth == self.S[:depth]:
                if root.left == None:
                    num = self.values.pop(0)
                    digits = len(str(num))
                    tmp = TreeNode(num)
                    self.S = self.S[depth + digits:]
                    create_tree(tmp, depth + 1)
                    root.left = tmp
                if root.right == None and '-' * depth == self.S[:depth]:
                    num = self.values.pop(0)
                    digits = len(str(num))
                    tmp = TreeNode(num)
                    self.S = self.S[depth + digits:]
                    create_tree(tmp, depth + 1)
                    root.right = tmp
                return root
            elif '-' * depth != self.S[:depth]:
                return
        return create_tree(root, 1)
