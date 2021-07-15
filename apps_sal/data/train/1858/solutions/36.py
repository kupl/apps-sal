# things learnt ..
# Try to check the first attempt and see if you can find the mistake
# we need a set or seen here .. 


# Second Attempt
class FindElements:
    
    def __init__(self, root: TreeNode):
        
        # fill using top down approach
        self.result = []
        q = []
        if root is None:
            return False
        q.append((root, 0))
        self.result.append(0)
        while len(q) > 0 :
            node, value = q.pop(0)
            #print(\" node \", node)
            #print(\"value is \", value)
            if node.left is not None:
                temp = (value*2) +1
                self.result.append(temp)
                q.append((node.left, temp))
                
                
            if node.right is not None:
                temp = (value*2) +2
                self.result.append(temp)
                q.append((node.right, temp))
        print((self.result))
        
    def find(self, target: int) -> bool:
        return True if target in self.result else False
        
        




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# first attempt
# below code almost looks ok , but it doesn't pass all test cases.

# class FindElements:
#     result = []
#     def __init__(self, root: TreeNode):
#         #result = []
        
#         # fill using top down approach
#         def helper(root, value):
#             #base
#             if root.left is None and root.right is None:
#                 self.result.append(value)
#             #recursion
#             elif root.left is not None:
#                 self.result.append(value)
#                 temp = (value*2) +1
#                 helper(root.left, temp )
#                 #print(\"left not null\")
#                 #print(\"self.result \", self.result)
#             elif root.right is not None:
#                 self.result.append(value)
#                 temp = (value*2) +2
#                 helper(root.right, temp )
#                 #print(\"right not null\")
#                 #print(\"self.result \", self.result)
        
#         if root is None:
#             return False
#         helper(root, 0)
#         print(self.result)
#         return 
        
        

#     def find(self, target: int) -> bool:
#         return True if target in self.result else False
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

