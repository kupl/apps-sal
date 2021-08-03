class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dic = {}
        for i in range(len(matrix)):
            a = ''
            b = ''
            for j in range(len(matrix[0])):
                a = a + '%d' % matrix[i][j]
                b = b + '%d' % (1 - matrix[i][j])
       #     print(a,b,dic)
            if a not in dic:
                dic[a] = 1
            else:
                dic[a] += 1
            if b not in dic:
                dic[b] = 1
            else:
                dic[b] += 1
        m = 0
        # print(dic)
        for k in dic.keys():
            m = max(m, dic[k])
        return m
