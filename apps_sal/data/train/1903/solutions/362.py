# int minCostConnectPoints(vector<vector<int>>& ps) {
#     int n = ps.size(), res = 0, i = 0, connected = 0;
#     vector<bool> visited(n);
#     priority_queue<pair<int, int>> pq;
#     while (++connected < n) {
#         visited[i] = true;
#         for (int j = 0; j < n; ++j)
#             if (!visited[j])
#                 pq.push({-(abs(ps[i][0] - ps[j][0]) + abs(ps[i][1] - ps[j][1])), j});
#         while (visited[pq.top().second])
#             pq.pop();
#         res -= pq.top().first;
#         i = pq.top().second;
#         pq.pop();
#     }
#     return res;
# }

class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        n, vis, ans, pq, i = len(a), set([0]), 0, [], 0
        rem = set(range(1, n))
        while len(vis) < n:
            for j in rem:
                heappush(pq, (abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1]), j))
            while pq[0][1] in vis:
                heappop(pq)
            val, i = heappop(pq)
            vis.add(i)
            rem.discard(i)
            ans += val
        return ans
