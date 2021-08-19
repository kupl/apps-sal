class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:

        def hashing(i, j, p=40001):
            return i * p + j
        board = set()
        for (x, y) in points:
            board.add(hashing(x, y))
        ans = float('inf')
        print(board)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                (tlx, tly) = points[i]
                (brx, bry) = points[j]
                if tlx == brx or tly == bry:
                    continue
                if hashing(tlx, bry) in board and hashing(brx, tly) in board:
                    ans = min(ans, abs((brx - tlx) * (bry - tly)))
        if ans < float('inf'):
            return ans
        else:
            return 0
