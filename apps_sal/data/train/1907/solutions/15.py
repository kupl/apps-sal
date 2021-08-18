
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def wtf(root, target):
            if root.val == target.val:
                print('a')
                return root
            if root.left:
                print('b')
                ans = wtf(root.left, target)
                if ans != None:
                    return ans
            if root.right:
                print('c')
                ans = wtf(root.right, target)
                if ans != None:
                    return ans
            return
        return wtf(cloned, target)
