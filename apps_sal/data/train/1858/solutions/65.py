# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        stack=[root]
        root.val=0
        self.l=[]
        while stack:
            r=stack.pop()
            self.l.append(r.val)
            if r.left:
                stack.append(r.left)
                r.left.val=2*r.val+1
            if r.right:
                stack.append(r.right)
                r.right.val=2*r.val+2
        #print(self.l)
        

    def find(self, target: int) -> bool:
        return target in self.l
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

