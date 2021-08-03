# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def recover(self, root, val):
        root.val = val
        if root.left:
            self.recover(root.left, 2*val+1)
        if root.right:
            self.recover(root.right, 2*val+2)
    
    def __init__(self, root: TreeNode):
        self.recover(root, 0)
        self._root = root

    def find(self, target: int) -> bool:
        ops = []
        while target > 0:
            if target % 2 == 1:
                ops = [\"l\"] + ops
                target = (target-1)//2
            else:
                ops = [\"r\"] + ops
                target = (target-2)//2
        assert target==0
        node = self._root
        for op in ops:
            node = node.left if op == 'l' else node.right
            if not node:
                return False
        return True
            
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
