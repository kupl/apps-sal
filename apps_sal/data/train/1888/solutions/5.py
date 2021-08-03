class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            nrt = TreeNode(v)
            nrt.left = root
            return nrt
        level = 1
        que = [root]
        d -= 1
        beg, end = 0, 1
        while beg < end:
            lev_cnt = 0
            i = beg
            if level == d:
                while i < end:
                    p = que[i]
                    lt, rt = TreeNode(v), TreeNode(v)
                    lt.left = p.left
                    p.left = lt
                    rt.right = p.right
                    p.right = rt
                    i += 1
                return root
            while i < end:
                p = que[i]
                if p.left:
                    que.append(p.left)
                    lev_cnt += 1
                if p.right:
                    que.append(p.right)
                    lev_cnt += 1
                i += 1
            beg = end
            end += lev_cnt
            level += 1
        return root
