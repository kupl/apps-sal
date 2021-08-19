class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 1
        for x, y in points:
            angles = []
            for x1, y1 in points:
                if (x1 != x or y1 != y) and (d := sqrt((x1 - x)**2 + (y1 - y)**2)) <= 2 * r:
                    angle = atan2(y1 - y, x1 - x)
                    delta = acos(d / (2 * r))
                    angles.append((angle - delta, +1))  # entry
                    angles.append((angle + delta, -1))  # exit
            angles.sort(key=lambda x: (x[0], -x[1]))
            val = 1
            for _, entry in angles:
                ans = max(ans, val := val + entry)
        return ans


# https://www.geeksforgeeks.org/angular-sweep-maximum-points-can-enclosed-circle-given-radius/
#        class Solution {
#    public int numPoints(int[][] points, int r) {
#        int count = 1;
#        for(int i = 0; i < points.length; i++) {
#            Map<Double, Integer> angles = new HashMap<>();
#            for(int j = 0; j < points.length; j++) {
#                if (i != j) {
#                    if (points[i][0] != points[j][0] || points[i][1] != points[j][1]) {
#                        int d = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) * (points[i][1] - points[j][1]);
#                        double angle = Math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0]);
#                        double delta = acos(d / (2 * r));
#                        double entry = angle - delta;
#                        double exit = angle + delta;
#                        map.put(entry, map.getOrDefault(entry, 0) + 1);
#                        map.put(exit, map.getOrDefault(exit, 0) - 1);
#                    }
#                }
#            }
#            Map<String, Integer> result = angles.entrySet().stream()
#                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
#                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
#                        (oldValue, newValue) -> oldValue, LinkedHashMap::new));
#
#        }
#        return count;
#    }
# }
