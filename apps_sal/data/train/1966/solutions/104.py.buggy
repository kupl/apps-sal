class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def num(mat,i,j):
            result = 0
            index_i = i
            
            while index_i<len(mat) and mat[index_i][j] == 1:
                result += 1
                index_i += 1
            index_j = j
            while index_j<len(mat[0]) and mat[i][index_j] == 1:
                result += 1
                index_j += 1
                
            result -= 1
            print(result)
            bound_i = index_i
            bound_j = index_j
            for row in range(i+1,bound_i):
                for col in range(j+1,bound_j):
                    if mat[row][col] == 1:
                        result += 1
                    else:
                        bound_i = row
                        bound_j = col
                        break
                        
            return result
        \"\"\"
        if len(mat) == 0 or len(mat[0]) == 0:
            return 0
        
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    n = num(mat,i,j)
                    print(n)
                    result += n
        return result
        \"\"\"
        
        \"\"\"
        #O(n*n*m)
        row = [[0]*len(mat[0]) for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if j == 0:
                        row[i][j] = 1
                    else:
                        row[i][j] = row[i][j-1] + 1
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if i == 0:
                        result += row[i][j]
                    else:
                        result += row[i][j]
                        index = i - 1
                        bound = row[i][j]
                        while index>=0:
                            bound = min(bound,row[index][j])
                            if bound == 0:
                                break
                            result += min(row[i][j],bound)
                            index = index - 1
        return result
        \"\"\"
        
        row = [[0]*len(mat[0]) for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if j == 0:
                        row[i][j] = 1
                    else:
                        row[i][j] = row[i][j-1] + 1
        result = 0
        
        for j in range(len(mat[0])):
            stack = []
            total = 0
            for i in range(len(mat)):
                height = 1
                while len(stack)>0 and stack[-1][0]>row[i][j]:
                    total -= stack[-1][1]*(stack[-1][0] - row[i][j])
                    height += stack[-1][1]
                    stack.pop()
                total += row[i][j]
                result += total
                stack.append([row[i][j],height])
        return result
        
        
        
        
        
        
