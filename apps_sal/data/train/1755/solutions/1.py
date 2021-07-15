#Re-use of my  dynamic programing approach for spliting the workload part I
#Given a set S of n non-negative integers:
# 1) make a partition of S with exactly two subsets A,B of S, such that the absolute
#    difference of the elements of each set is minimized

#To solve this problem, all we need to do is use the general subset sum program, but
# set the target sum to S/2 where S is the sum of all of the elements in the list
from collections import Counter     #for differencing lists with (possible) duplicates


#Build the dynamic programing table:  Column are the sums, and rows are the subsets
#   DP[i][j] == True if and only if there exists a subset of {a[0],...,a[i-1]} such
#               that the a[0]+...+a[i-1]==j 
# Row i is the subset {a[0],...,a[i-1]}
# Col j is a number (representing a sum)
#The function additionally builds a 'parent' table that is used to determine
# the optimal path (which will allow us to get the elements in the subsets)
def getdDPTable( numList, sizeList, targetSum):

    numRows = sizeList + 1       #to account for empty set, we need +1
    numCols  = targetSum + 1     #to account for zero, we need +1

    #initialize both tables
    dp     = [ [False for _ in range(numCols)] for _ in range(numRows) ]
    parent = [ [ []   for _ in range(numCols)] for _ in range(numRows) ]

    #The sum of 0 can be achieved by selecting no elements from each possible subsets
    #  That is, it is true we can always acheive the sum of 0 from any possible subset
    for r in range(numRows):
        dp[r][0] = True
    
    #increasing in rows, and from left to right wrt columns, we build the rest
    # of the DP table row i corresponds to the set {a_0,...,a_i}, column j
    # corresponds to the target sum j.  If d[i][j] is true, that means there
    # exists a subset of  {a_0,...,a_i} whose elemenst sum to j 
    for r in range(1, numRows):
        for c in range(1, numCols):
            if c < numList[r-1]:            #on row r, current column is less than numList[r-1]
                dp[r][c] = dp[r-1][c]       #see row above for whether there exists a subeset that sums to j
                parent[r][c].append(tuple( [r-1, c] ))   #we store where we got the answer
            else:                           #we must perform a backtrack on the previous row
                alreadyBuilt = dp[r-1][c]                           #look at row above
                isInOriginalNumList   = dp[r-1][c - numList[r-1]]   #look at backtrack
                dp[r][c] = alreadyBuilt or isInOriginalNumList

                #we store the parent that is true
                if alreadyBuilt:
                    parent[r][c].append( tuple( [r-1, c] ) )
                if isInOriginalNumList:
                    parent[r][c].append( tuple( [r-1, c - numList[r-1]] ) )


    return dp, parent, numRows, numCols
#---end function


#Here, using the parent table that was built (when building the dynamic programming table)
# we extract the subset elements that form the optimal target sum
def getSubset(parent, numRows, targetSum):
    subset = []

    child   =  [tuple([numRows-1, targetSum])]
    cRow, cCol   = child[0][0], child[0][1]
    father =  parent[numRows-1][targetSum] 

    while father:
        fRow   =  father[0][0]
        fCol   =  father[0][1]
        
        diff = cCol - fCol
        if diff !=0 :
            subset.append(diff)
        
        cRow = fRow
        cCol = fCol
        father = parent[fRow][fCol]
    
    return subset     
#---end function



#In the scenario we can not find the best case scenario of a set with
#  the target sum of (sum of entire set)/2 (as then the difference would be 0)
# We must find the next best number, which is determined by the largest column
# in the DP table (as this corresponds to the largest possible sum that can be made) 
def getBestNum(dp, numList, targetSum, numRows):

    for j in range(targetSum,-1,-1):
        if dp[numRows-1][j]==True:      #found the largest sum we can make
            break

    return j
#---end function


#The main driver to solve the minimum partion problem
# Exmaple: [0, 20, 54, 99, 84, 99] has a minimum partion of ([99, 54, 20], [0, 99, 84]) 
#          that has a difference of 10
#First we try to partition the number list into equal valued sets (whose elements sum to
#  the same number).  If that works, we found that the min diff is 0, so make the two  
#  subsets and return them.  If we have a list of numbers where we can't partition them
#  into equal values, we have to find the largest possible sum we can make.  Then, simply
#  find the subset that makes that largest number, and we are done
def splitlist(numList):
    
    sizeList = len(numList)

    #First see if we can get a subset that sums to sum(numList)//2 (then diff would be zero)
    targetSum = sum(numList)//2 
    dp, parent, numRows, numCols = getdDPTable(numList, sizeList, targetSum)
    
    foundSubset = dp[numRows-1][targetSum]

    bestDiff = 0
    if foundSubset:     #We found a subset whose elements sum to the target sum(numList)//2
        subsetA = getSubset(parent, numRows, targetSum)
    else:
        #We could not get the best case senario, so we need to find the largest possible subset
        # sum tha we can make given the provided list of numbers (see e.x. [0, 20, 54, 99, 84, 99])
        newTargetSum = getBestNum(dp, numList, targetSum, numRows)
        dp, parent, numRows, numCols = getdDPTable(numList, sizeList, newTargetSum)
        subsetA = getSubset(parent, numRows, newTargetSum)

    #partition the provided list of numbers into two subsets A and B
    c1 = Counter(numList)
    c2 = Counter(subsetA)
    diff = c1-c2
    subsetB = list(diff.elements())
    
    return subsetA, subsetB
#---end function

