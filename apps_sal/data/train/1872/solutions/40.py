from collections import deque


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        mx = root.val
        mxlvl = 1
        if root.right is None and root.left is None:
            return 1

        clvl = 2
        s = 0

        q = deque()
        q.append((root.right, 2))
        q.append((root.left, 2))
        while q:
            n, lvl = q.popleft()
            if n is None:
                continue
            if lvl == clvl:
                s += n.val
                print((s, clvl))
            else:
                if s > mx:
                    mx = s
                    mxlvl = clvl
                    mx = s
                s = n.val
                clvl = lvl
            q.append((n.left, lvl + 1))
            q.append((n.right, lvl + 1))
        if s > mx:
            mx = s
            mxlvl = clvl
        return mxlvl
