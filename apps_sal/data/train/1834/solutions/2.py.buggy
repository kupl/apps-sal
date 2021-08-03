class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            if A[i][0] == 0:
                A[i] = [j^1 for j in A[i]]

        A = list(map(list, zip(*A)))        

        for i in range(len(A)):
            if sum(A[i]) < len(A[i])/2:
                A[i] = [j^1 for j in A[i]]

        A = list(map(list, zip(*A)))  

        summ = 0
        for i in A:
            summ += int(\"\".join(str(x) for x in i), 2) 

        return summ   
