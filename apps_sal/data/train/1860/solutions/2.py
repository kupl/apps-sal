class Solution:
     def fallingSquares(self, positions):
         """
         :type positions: List[List[int]]
         :rtype: List[int]
         
         COORDINATE COMPRESSION IS THE WAY TO GO - CHECKOUT OFFICAL LEETCODE ANSWER.  THIS WORKS TOO.
         """
 #         if positions == []: return []
 #         def overlap(int1, int2):
 #             return not (int1[0] > int2[1] or int1[1] < int2[0])
 
 # #       sorted disjoint interval list
 #         ints = [positions[0][0], positions[0][0]+positions[0][1]-1] # forgot to make this x+y-1 - wrote y
 #         intheights = {(positions[0][0], positions[0][0]+positions[0][1]-1): positions[0][1]} # same as above
 #         maxheights = [positions[0][1]]
         
 #         for i in range(1, len(positions)):
 #             # print(positions[i], ints, intheights)
 #             start2 = positions[i][0]
 #             end2 = positions[i][0] + positions[i][1] - 1
             
 #             leftpos = bisect.bisect_left(ints, start2)
 #             rightpos = bisect.bisect_right(ints, end2)
 #             newints = ints[:(leftpos // 2 * 2)]
 #             if leftpos % 2 == 1:
 #                 newints.append(ints[leftpos-1])
 #                 newints.append(start2-1)
 #                 intheights[(ints[leftpos-1], start2-1)] = intheights[(ints[leftpos-1], ints[leftpos])]
             
 #             left = leftpos // 2 * 2
 #             right = (rightpos + 1) // 2 * 2
 #             maxSoFar = 0
 #             lastheight = 0
 #             while left < right:
 #                 maxSoFar = max(maxSoFar, intheights[(ints[left], ints[left+1])])
 #                 lastheight = intheights[(ints[left], ints[left+1])]
 #                 del intheights[(ints[left], ints[left+1])]
 #                 left += 2
             
 #             newints.append(start2)
 #             newints.append(end2)
 #             intheights[(start2, end2)] = maxSoFar + (end2-start2+1)
 #             maxheight = max(maxheights[-1], intheights[(start2, end2)])
 #             maxheights.append(maxheight)
 
 #             if rightpos % 2 == 1:
 #                 newints.append(end2+1)
 #                 newints.append(ints[rightpos])
 #                 intheights[(end2+1, ints[rightpos])] = lastheight
 #             newints.extend(ints[right:])  # forgot this line
 #             ints = newints
             
             
 #         return maxheights
         ints = []
         for left, size in positions:
             ints.append(left)
             ints.append(left+size-1)
         
         index = {num:idx for idx, num in enumerate(sorted(ints))}
         heights = [0]*2*len(positions)
         
         def query(left, right):
             return max(heights[index[left]: index[right]+1])
         
         def updateHeights(left, right, newheight):
             for i in range(index[left], index[right]+1):
 #                 no need for max here.  You are updating unless the height is negative
                 heights[i] = newheight
         
         maxheights = []
         for left, size in positions:
             right = left+size -1
             newheight = query(left, right) + size
             updateHeights(left, right, newheight)
             if not maxheights or maxheights[-1] <= newheight:
                 maxheights.append(newheight)
             else:
                 maxheights.append(maxheights[-1])
         
         return maxheights
             

