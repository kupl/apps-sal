# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return(self.helper(root)[1])

    def helper(self, root, myMax=0):
        myList = []
        if root.left:
            temp1, temp2 = self.helper(root.left)
            myList.extend(temp1)
            if temp2 > myMax:
                myMax = temp2
        if root.right:
            temp1, temp2 = self.helper(root.right)
            myList.extend(temp1)
            if temp2 > myMax:
                myMax = temp2
        myList.append(root.val)
        for i in range(len(myList) - 1):
            if abs(root.val - myList[i]) > myMax:
                myMax = abs(root.val - myList[i])
        return (myList, myMax)
