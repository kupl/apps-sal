class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0][0]
        firstRow = arr[0]
        srow = sorted([(num, idx) for idx, num in enumerate(firstRow)])
        cand1, cand2 = srow[0], srow[1]
        for row in arr[1:]:
            srow = sorted([(num, idx) for idx, num in enumerate(row)])
            num1, idx1 = srow[0][0], srow[0][1]
            num2, idx2 = srow[1][0], srow[1][1]
            c1v = min(float('inf') if cand1[1] == idx1 else cand1[0] + num1,
                      float('inf') if cand2[1] == idx1 else cand2[0] + num1)
            c2v = min(float('inf') if cand1[1] == idx2 else cand1[0] + num2,
                      float('inf') if cand2[1] == idx2 else cand2[0] + num2)
            cand1 = (c1v, idx1)
            cand2 = (c2v, idx2)
        return min(cand1[0], cand2[0])
