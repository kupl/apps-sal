class Solution:
     def maxChunksToSorted(self, arr):
         """
         :type arr: List[int]
         :rtype: int
         """
         dict = {}           #存储排序后的每个元素的位置
         sortedArr = sorted(arr)
         for i in range(len(sortedArr)):
             if(sortedArr[i] not in dict):
                 dict[sortedArr[i]] = [i]
             else:
                 dict[sortedArr[i]].append(i)
 
         position = []       #存储每个元素相对排序后的数组应该移动的距离
         for i, val in enumerate(arr):
             position.append(dict[val][0] - i)
             dict[val].pop(0)           #可能有重复元素，那么在使用完一个元素后，就把使用过的元素位置删除
 
 
         maxNum = 0
         i = 0
         ifPlusMinus = 0         #用于判断是否需要移动0位置的数包含在需要左右都移动的数之间，如[4,3,2,1,0]
                                 #该数组中2是不移动的，但因为4，3和1，0都要移动，所以不能单独另算
         maxIdealPosition = 0   #用于存储要移动子数组中左侧元素向右移动的最大距离
         while(i < len(position)):
             if(position[i] == 0 and ifPlusMinus == 0):
                 maxNum += 1
                 i += 1
             elif(position[i] > 0 and ifPlusMinus == 0):     #要移动的子数组中处于"最左面最开始位置"需要"右移"的数，它一定会匹配到最右侧position是负数的数
                 ifPlusMinus = 1
                 maxIdealPosition = i + position[i]
                 i += 1
             elif(position[i] >= 0 and ifPlusMinus == 1):    #处于要移动子数组的"中间位置"
                 if(i + position[i] > maxIdealPosition):     #查看是否需要更新maxIdealPosition值，如arr=[1,2,0,3],position=[1,1,-2,0]
                     maxIdealPosition = i + position[i]
                 i += 1
             elif(position[i] <0 and ifPlusMinus == 1):      #处于要移动子数组的"末尾位置"
                 if(i < len(position) - 1):
                     if(position[i+1] < 0):
                         i += 1
                     elif(position[i+1] >= 0):
                         if(i == maxIdealPosition):        #判断是否已扫描到要移动数组中需要右移数组的最大理想位置
                             maxNum += 1
                             ifPlusMinus = 0
                             maxIdealPosition = 0
                         i += 1
                 else:
                     maxNum += 1
                     ifPlusMinus = 0
                     i += 1
 
         return maxNum
