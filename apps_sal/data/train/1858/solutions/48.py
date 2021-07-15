# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        
        self.d = collections.defaultdict(int)
        def recover(root,l,r,p):
            if not l and not r:
                root.val = 0
                
            elif r and not l:
                
                root.val = 2*p+2
            elif l and not r:
                root.val = 2*p+1
            self.d[root.val]+=1
            if root.left: root.left = recover(root.left, True, False, root.val)
            if root.right: root.right = recover(root.right, False, True, root.val)
            return root
        if root:
            node = recover(root, False,False, None)
        
                
            
            
            
        

    def find(self, target: int) -> bool:
        return (target in self.d)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

