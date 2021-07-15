# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        li=['null']
        self.y=set()
        def dfs(root,v):
            if(root):
                root.val=v
                self.y.add(root.val)
                dfs(root.left,2*v+1)
                dfs(root.right,2*v+2)
        dfs(root,0)
        print((self.y))
    def find(self, target: int) -> bool:
        if target in self.y:
            return True
        else:
            return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

