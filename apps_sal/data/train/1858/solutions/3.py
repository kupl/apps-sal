# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        
    def find(self, target: int) -> bool:
        
        stack=[]
        if target ==0 and self.root:
            return True
        
        while target>0:
            if target%2:
                target=(target-1)/2
                stack.append(\"left\")
            else:
                target=(target-2)/2
                stack.append(\"right\")
                
        node=self.root
        if not node or not stack:
            return False
        
        while stack:
            path=stack.pop()
            if path==\"left\":
                node=node.left
                if not node:
                    return False
            else:
                node=node.right
                if not node:
                    return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        # q=[self.root]
        # while q:
        #     width=len(q)
        #     for _ in range(width):
        #         node=q.pop(0)
        #         if node.val == target:
        #             return True
        #         if node.left:
        #             node.left.val=node.val*2+1
        #             q.append(node.left)
        #         if node.right:
        #             node.right.val=node.val*2+2
        #             q.append(node.right)
        # return False
    
    # def fix_tree(self,root,val):
    #     if not root:
    #         return None
    #     root.val=val
    #     root.left=self.fix_tree(root.left,val*2+1)
    #     root.right=self.fix_tree(root.right,val*2+2)
    #     self.max = max(self.max,val)
    #     return root


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
