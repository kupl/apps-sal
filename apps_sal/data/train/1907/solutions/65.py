class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def find_node(orignal, copy, find):
            if not orignal:
                return None
            if orignal == find:
                return copy
            return find_node(orignal.left, copy.left, find) or find_node(orignal.right, copy.right, find)
        return find_node(original, cloned, target)
