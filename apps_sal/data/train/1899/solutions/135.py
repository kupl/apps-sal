class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        '''
        [1 1 1 1 1]
        [1 0 0 0 1]
        [1 0 1 0 1]
        [1 0 0 0 1]
        [1 1 1 1 1]

        [0 2 0]
        [0 0 0]
        [0 0 1]

        Find one island - convert all of it to 2. then put them all in queue. Find all non-2's that are 1 away as next frontier.
        Check if you ever reach 1
        '''
        def isvalid(row, col):
            return 0 <= row < len(A) and 0 <= col < len(A[0])

        def dfs(row, col):
            if not isvalid(row, col) or A[row][col] != 1:
                return
            A[row][col] = 2
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row = row + i
                new_col = col + j
                dfs(new_row, new_col)
            return

        found = False
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] == 1:
                    dfs(row, col)
                    found = True
                    break
            if found:
                break

        twos = []
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] == 2:
                    twos.append((row, col))
        steps = 0
        while twos:
            next_ = []
            steps += 1
            for point in twos:
                row, col = point
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row = row + i
                    new_col = col + j
                    if isvalid(new_row, new_col) and A[new_row][new_col] == 0:
                        A[new_row][new_col] = -1
                        next_.append((new_row, new_col))
                    elif isvalid(new_row, new_col) and A[new_row][new_col] == 1:
                        return steps - 1
            twos = next_
        return -1
