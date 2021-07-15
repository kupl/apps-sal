# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.all=[]
        def helperIter(root):
            val =0
            if not root:
                return
            
            stack = [(root, val)]
            while stack:
                curr, val = stack.pop()
                curr.val = val
                if curr.left:
                    self.all.append(2*val+1)
                    stack.append((curr.left, 2*val +1))
                if curr.right:
                    self.all.append(2*val +2)
                    stack.append((curr.right, 2*val +2))
            
        def helper(root, val):
            if not root:
                return

            if root:
                root.val= val
                self.all.append(val)
            
            if root.left:
                helper(root.left, 2*val +1)
            if root.right:
                helper(root.right, 2*val +2)
        
        # helper(root, 0)
        helperIter(root)
        
                    

    def find(self, target: int) -> bool:
        return target in self.all


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

