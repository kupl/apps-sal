class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        ht = {}
        '''
        create a hash table, keys is the pos list of 0 and pos list of 1 in a row
        because they represent for 
        count 
        ans = max value of keys
        '''
        for r in range(row):
            need = [[], []]
            for c in range(col):
                if matrix[r][c] == 0:
                    need[0].append(c)
                else:
                    need[1].append(c)
            a = str(need[0])
            b = str(need[1])
            if a in ht:
                ht[a] += 1
            else:
                ht[a] = 1
            if b in ht:
                ht[b] += 1
            else:
                ht[b] = 1

        val = list(ht.values())
        ans = max(val)
        return ans
