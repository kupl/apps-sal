class Solution:

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def calcdeep(root, d, level):
            if level not in d:
                d[level] = []
            d[level].append(root)
            r1 = r2 = level
            if root.left != None:
                r1 = calcdeep(root.left, d, level + 1)
            if root.right != None:
                r2 = calcdeep(root.right, d, level + 1)
            return max(r1, r2)
        d = dict()
        maxl = calcdeep(root, d, 0)
        if len(d[maxl]) == 1:
            return d[maxl][0]

        def check2(root, ts, prefix, d):
            if root == None:
                return
            prefix.append(root)
            if root in ts:
                d[root.val] = copy.deepcopy(prefix)
            check2(root.left, ts, prefix, d)
            check2(root.right, ts, prefix, d)
            prefix.pop()
        targets = d[maxl]
        d = dict()
        prefix = []
        check2(root, targets, prefix, d)
        idx = maxl - 1
        while idx >= 0:
            vals = list(d.values())
            t = vals[0][idx]
            failed = False
            for val in list(d.values()):
                if val[idx].val != t.val:
                    failed = True
                    break
            if failed == False:
                return t
            idx -= 1
        return None
