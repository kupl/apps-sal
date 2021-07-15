# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        res = []
        def helper(node, parentVal = None, left = False, right = False):
            if node:
                if parentVal is None:
                    # node.val = 0 #root
                    val = 0
                    res.append(val)
                else:
                    if left:
                        # node.val = parent.val*2 + 1
                        val = parentVal*2 + 1
                        res.append(val)
                    if right:
                        # node.val = parent.val*2 + 2
                        val = parentVal*2 + 2
                        res.append(val)
                helper(node.left, val, True, False)
                helper(node.right, val, False, True)
        helper(root)
        self.res = set(res)
        print(root)
        

    def find(self, target: int) -> bool:
        return target in self.res


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

