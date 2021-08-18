class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def dfs(s, idx, depth):
            if idx == len(s):
                return None, len(s)
            cnt = 0
            while s[cnt + idx] == '-':
                cnt += 1

            if cnt != depth:
                return None, idx

            idx += cnt
            i = 0
            while idx + i < len(s) and s[idx + i].isdigit():
                i += 1
            root = TreeNode(int(s[idx:idx + i]))
            idx += i
            root.left, li = dfs(s, idx, depth + 1)
            root.right, ri = dfs(s, li, depth + 1)
            return root, ri

        return dfs(S, 0, 0)[0]
