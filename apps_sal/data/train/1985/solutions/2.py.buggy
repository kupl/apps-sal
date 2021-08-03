def subtable(fromX, toX, fromY, toY, table, value):
 	# smalltable = table[fromX:toX, fromY:toY]
 	# midpoint = math.floor(len(smalltable) / 2)
 	# if len(smalltable[0]) == 1:
 	# 	if smalltable[0] == value:
 	# 		return (fromX, fromY)
 	# 	else:
 	# 		return (-1, -1)
 	# if subtable[midpoint][midpoint] == value:
 	# 	return (midpoint, midpoint)
 	# if subtable[midpoint][midpoint] < value:
 	# 	bottomRight = subtable(math.floor(0), len(smalltable[0]), math.floor((fromY + toY) / 2), len(smalltable), table, value)
 	# if subtable[midpoint][midpoint] > value:
 	# 	topLeft = subtable(0, math.floor((fromX + toX) / 2), 0, math.floor((fromY + toY) / 2), table, value)
 	midpointX = (fromX + toX)//2
 	midpointY = (fromY + toY)//2
 	if (toX - fromX < 2 and toY - fromY < 2):
 		if fromX == toX or fromY == toY:
 			return (-1,-1)
 		if table[fromX][fromY] == value:
 			return (fromY, fromX)
 		else:
 			return (-1, -1)
 	if table[midpointX][midpointY] == value:
 		return (midpointY, midpointX)
 	topLeft = (-1, -1)
 	if table[midpointX][midpointY] > value:
 		topLeft = subtable(fromX, midpointX, fromY, midpointY, table, value)
 	bottomRight = (-1, -1)
 	if table[midpointX][midpointY] < value:
 		bottomRight = subtable(midpointX, toX, midpointY, toY, table, value)
 	topRight = subtable(midpointX, toX, fromY, midpointY, table, value)
 	bottomLeft = subtable(fromX, midpointX, midpointY, toY, table, value)
 	if topLeft != (-1,-1):
 		return topLeft
 	elif bottomRight != (-1,-1):
 		return bottomRight
 	elif topRight != (-1, -1):
 		return topRight
 	elif bottomLeft != (-1, -1):
 		return bottomLeft
 	else:
 		return (-1, -1)
 
 def find(table, val):
 	#replace the body of this function to return the index of 'val' within the 2D array 'table' as a tuple of integers
 	#if 'val' appears nowhere in 'table' then return '(-1, -1)'
 	# midpoint = math.floor(len(table) / 2)
 	# print(table)
 	# if len(table[0]) == 0:
 	# 	return (-1,-1)
 	# if table[midpoint][midpoint] == val:
 	# 	return (midpoint, midpoint)
 	# else:
 	# 	if table[midpoint][midpoint] < val:
 	# 		return find(table[:(midpoint), :(midpoint + 1)], val)
 	# 	if table[midpoint][midpoint] > val:
 	# 		return find(table[midpoint:, (midpoint+1):], val)
     if len(table) == 0 or len(table[0]) == 0:
         return (-1, -1)
     else:
         return subtable(0, len(table), 0, len(table[0]), table, val)
 
 class Solution:
     def searchMatrix(self, matrix, target):
         if find(matrix, target) == (-1, -1):
             return False
         else:
             return True
         
