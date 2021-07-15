# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def rebuild(self,root:TreeNode):
        queue=[]
        root.val=0
        queue.append(root)
        while queue:
            new=queue.pop(0)
            if new.left:
                new.left.val=2*new.val+1
                self.collection.append(new.left.val)
                queue.append(new.left)
            if new.right:
                new.right.val=2*new.val+2
                self.collection.append(new.right.val)
                queue.append(new.right)

    def __init__(self, root: TreeNode):
        self.copy=root
        self.collection=[0]
        self.rebuild(self.copy)
        
        
    def find(self, target: int) -> bool:

        return target in self.collection
    



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

