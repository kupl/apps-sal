class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        score = [-1] * len(points)
        total_score = 0
        for i in range(1, len(points)):
            x, y = points[i - 1][0], points[i - 1][1]
            cur_min_idx, cur_min_val = -1, -1
            for j in range(i, len(points)):
                cur_dist = abs(x - points[j][0]) + abs(y - points[j][1])
                if score[j] == -1:
                    score[j] = cur_dist
                elif cur_dist < score[j]:
                    score[j] = cur_dist
                if cur_min_val == -1 or score[j] < cur_min_val:
                    cur_min_val, cur_min_idx = score[j], j
            total_score += cur_min_val
            if i != j:
                score[cur_min_idx], score[i] = score[i], score[cur_min_idx]
                points[cur_min_idx], points[i] = points[i], points[cur_min_idx]
        return total_score
