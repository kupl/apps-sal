class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return

        def recur(ori, clo, target):
            if not ori:
                return
            if ori is target:
                return clo
            else:
                temp = recur(ori.left, clo.left, target)
                temp2 = recur(ori.right, clo.right, target)
                if temp:
                    return temp
                if temp2:
                    return temp2
        return recur(original, cloned, target)
