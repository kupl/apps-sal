class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        answer = []
        r = 0
        c = 0

        for i in range(len(mat)):
            tmp = []
            for j in range(len(mat[0])):
                if i - K < 0:
                    r = 0
                else:
                    r = i - K

                sum1 = 0
                while r <= i + K and r < len(mat):
                    if j - K < 0:
                        if j + K < len(mat[0]):
                            sum1 += sum(mat[r][:j + K + 1])
                        else:
                            sum1 += sum(mat[r])
                    else:
                        if j + K < len(mat[0]):
                            sum1 += sum(mat[r][j - K:j + K + 1])
                        else:
                            sum1 += sum(mat[r][j - K:])

                    r += 1
                tmp.append(sum1)
            answer.append(tmp)
        return answer
