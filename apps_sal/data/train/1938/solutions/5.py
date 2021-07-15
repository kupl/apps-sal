class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        Xs = [x for x1, _, x2, _ in rectangles for x in [x1, x2]]
        Xs.sort()
        X_idx_lookup = {x: idx for idx, x in enumerate(Xs)}
        
        res = 0
        prev_y = 0
        X_span = 0
        
        Ys = [e for x1, y1, x2, y2 in rectangles for e in [[y1, x1, x2, 1], [y2, x1, x2, -1]]]
        Ys.sort()
        
        overlap_count = [0] * len(Xs)
        
        for y, xl, xr, inout in Ys:
            res += (y - prev_y) * X_span
            prev_y = y
            start_idx, end_idx = X_idx_lookup[xl], X_idx_lookup[xr]
            for i in range(start_idx, end_idx):
                overlap_count[i] += inout
            X_span = sum(x2 - x1 if c > 0 else 0 for x1, x2, c in zip(Xs, Xs[1:], overlap_count))
        return res % 1000000007

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        Xs = [x for x1, _, x2, _ in rectangles for x in [x1, x2]]
        Xs.sort()
        covered = [0] * len(Xs)
        res = 0
        
        keypoints = [e for x1, y1, x2, y2 in rectangles for e in [[y1, x1, x2, 1], [y2, x1, x2, -1]]]
        keypoints.sort()
        
        prev_y = 0
        width_span = 0
        for y, x1, x2, inout in keypoints:
            res += (y - prev_y) * width_span
            prev_y = y
            for i in range(len(covered) - 1):
                a, b = Xs[i], Xs[i + 1]
                if x1 <= a and b <= x2:
                    covered[i] += inout
            width_span = sum(Xs[i + 1] - Xs[i] if covered[i] > 0 else 0 for i in range(len(covered) - 1))
        return res % 1000000007
