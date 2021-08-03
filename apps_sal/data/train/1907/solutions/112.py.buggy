class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.path = 0
        self.targetNum = target.val
        self.dfs(original, 1)
        ansPath = str(bin(self.path))[3:]
        for i in ansPath:
            if(i == \"1\"):
                cloned = cloned.left
            else:
                cloned = cloned.right
        return cloned
    
    def dfs(self, curr, path):
        if(curr.val == self.targetNum):
            self.path = path
            return
        if(curr.left):
            self.dfs(curr.left, (path<<1) + 1)
        if(curr.right):
            self.dfs(curr.right, path<<1)
