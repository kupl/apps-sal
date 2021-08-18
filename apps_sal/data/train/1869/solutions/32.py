class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        idx = 0
        while idx < len(S) and S[idx] != '-':
            idx += 1
        root = TreeNode(int(S[:idx]))
        root_l = idx
        if len(S) == idx:
            return root
        d = 0
        while S[idx] == '-':
            d += 1
            idx += 1
        cnt = 0
        while idx < len(S):
            if S[idx] != '-':
                if cnt == d:
                    root.left = self.recoverFromPreorder(S[root_l + d:idx - d])
                    root.right = self.recoverFromPreorder(S[idx:])
                    break
                cnt = 0
            else:
                cnt += 1
            idx += 1
            if idx == len(S):
                root.left = self.recoverFromPreorder(S[root_l + d:])
        return root
