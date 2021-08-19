class Solution:

    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        if '-' not in S:
            return TreeNode(int(S))
        (dashes, ind, n) = (0, 1, len(S))
        while ind < n and S[ind] >= '0' and (S[ind] <= '9'):
            ind += 1
        root = TreeNode(S[:ind])
        while ind < n and S[ind] == '-':
            ind += 1
            dashes += 1
        left_ind = ind
        dashes_right = 0
        while ind < n:
            dashes_right = 0
            while ind < n and S[ind] >= '0' and (S[ind] <= '9'):
                ind += 1
            while ind < n and S[ind] == '-':
                dashes_right += 1
                ind += 1
            if dashes_right == dashes:
                break
        if dashes_right == dashes:
            root.left = self.recoverFromPreorder(S[left_ind:ind - dashes_right])
            root.right = self.recoverFromPreorder(S[ind:])
        else:
            root.left = self.recoverFromPreorder(S[left_ind:])
        return root
