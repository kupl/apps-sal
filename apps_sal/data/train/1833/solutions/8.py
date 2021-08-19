# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        #   找最深节点的公共父节点

        #   The values of the nodes in the tree are unique.

        #   第一次遍历，记录每个节点的深度。然后找到最深的节点
        #   如果只有一个，返回他自己。有多个的？

        #   第二次遍历，记录每个目标节点的路径(路径长度相同)。再从右边找最后一个相同的节点。

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

        #   寻找公共父节点啦
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
        # print(d)
        while idx >= 0:
            # print(idx)
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
