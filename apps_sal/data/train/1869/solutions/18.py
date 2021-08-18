class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        dashes = 0
        stk = []
        i = 0
        while i < len(S):
            s = S[i]
            if s.isnumeric():
                c = s
                while i + 1 < len(S) and S[i + 1].isnumeric():
                    c += S[i + 1]
                    i += 1
                while stk and dashes != stk[-1][1] + 1:
                    stk.pop()

                node = TreeNode(int(c))
                if stk and stk[-1][0].left:
                    stk[-1][0].right = node
                elif stk:
                    stk[-1][0].left = node
                stk.append((node, dashes))
                dashes = 0

            else:
                dashes += 1

            i += 1

        return stk[0][0]
