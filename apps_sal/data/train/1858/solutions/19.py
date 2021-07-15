# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        
        self.root = root
        self.container = set()
        
        def helper(root, val):

            if not root:
                return
            
            root.val = val
            #self.container.add(val)
            helper(root.left, root.val*2+1)
            helper(root.right, root.val*2+2)
                
        
        helper(self.root, 0)
        #print(self.root.val)
        return
            
    def find(self, target: int) -> bool:
        #遍历, 太慢
        #def bianli(root, target):
        #    if not root:
        #        return False
        #    
        #    if root.val == target:
        #        return True
        #    
        #    res = bianli(root.left,target) or bianli(root.right,target)
        #    return res
        #
        #return bianli(self.root, target)
        
        #因为这个tree的点不重复，所以可以找出唯一路径到target
        #那么将这个路径走一遍，如果不通就说明找不到
        
        def findpath(target):
            path = [target]
            while target:
                diff = 1 if target%2 else 2
                target = int((target - diff)/2)
                path.append(target)
                
            return path[::-1]
                
            
        def trav(node, depth, path):
            if depth> len(path):
                return False
            else:
                if not node:
                    return False
                if node.val == path[-1]:
                    return True
                #print(node.val)
                if node.val == path[depth]:
                    res = trav(node.left, depth+1, path) or trav(node.right, depth+1,path)
                    return res
            return False
        
                    
        path = findpath(target)
        #print(path)
        return trav(self.root, 0, path)
        
        # 还有种办法就是init的时候建个dict
        # 找的时候直接在dict里找
        # return target in self.container
                
            
            
            
            
        
            


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

