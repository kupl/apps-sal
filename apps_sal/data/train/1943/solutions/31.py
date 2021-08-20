class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        intervals = deque()
        while A and B:
            (a, b) = (A[-1], B[-1])
            (x, y) = (max(a[0], b[0]), min(a[1], b[1]))
            if x <= y:
                intervals.appendleft([x, y])
            (A if a > b else B).pop()
        return intervals
