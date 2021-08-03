class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0

        m, n = len(mat), len(mat[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    count += 1
                    up, left = i - 1, j - 1

                    while up >= 0 and mat[up][j] == 1:
                        up -= 1
                    count += i - up - 1

                    while left >= 0 and mat[i][left] == 1:
                        left -= 1
                    count += j - left - 1

                    k = i - 1
                    while k > up:
                        l = j - 1
                        if mat[k][l] == 0:
                            break
                        while l > left:
                            if mat[k][l] == 1:
                                count += 1
                                l -= 1
                            else:
                                left = l
                                break
                        k -= 1
        return count
