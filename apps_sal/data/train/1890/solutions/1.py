class Solution:
     def findBottomLeftValue(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         dealArr = []
         indexNum = self.dealTree(root, dealArr, 0)
         # print(indexNum, dealArr[indexNum - 1][0])
         return dealArr[indexNum - 1][0]
     def dealTree(self, root, dealArr, indexNum):
         if root == None:
             return indexNum
         # if not dealArr[indexNum]:
         if len(dealArr) <= indexNum :
             dealArr.append([])
         dealArr[indexNum].append(root.val)
         # print(root.val, dealArr, len(dealArr))
         indexNum1 = self.dealTree(root.left, dealArr, indexNum + 1)
         indexNum2 = self.dealTree(root.right, dealArr, indexNum + 1)
         return max(indexNum1, indexNum2)
