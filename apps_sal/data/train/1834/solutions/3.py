class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        maxsum = 0
        power = len(A[0])
        for row in A:
            for i in range(power):
                maxsum += 2**(power - 1 - i) * row[i]
        while True:
            change = False
            crow = False
            num = 0
            cursum = maxsum
            localsum = maxsum
            for row in range(len(A)):
                for i in range(power):
                    term = 2**(power - 1 - i)
                    if A[row][i] == 1:
                        cursum -= term
                    else:
                        cursum += term
                if cursum > maxsum:
                    change = True
                    maxsum = cursum
                    crow = True
                    num = row
                cursum = localsum
            for col in range(power):
                term = 2**(power - 1 - col)
                for row in range(len(A)):
                    if A[row][col] == 1:
                        cursum -= term
                    else:
                        cursum += term
                if cursum > maxsum:
                    change = True
                    maxsum = cursum
                    crow = False
                    num = col
                cursum = localsum
            if change:
                if crow:
                    for i in range(power):
                        A[num][i] = A[num][i] + (1 - 2 * A[num][i])
                else:
                    for row in range(len(A)):
                        A[row][num] = A[row][num] + (1 - 2 * A[row][num])
            if not change:
                return maxsum
