# int find(vector<int> &ds, int i) {
#     return ds[i] < 0 ? i : ds[i] = find(ds, ds[i]);
# }
# int minCostConnectPoints(vector<vector<int>>& ps) {
#     int n = ps.size(), res = 0;
#     vector<int> ds(n, -1);
#     vector<array<int, 3>> arr;
#     for (auto i = 0; i < n; ++i)
#         for (auto j = i + 1; j < n; ++j) {
#             arr.push_back({abs(ps[i][0] - ps[j][0]) + abs(ps[i][1] - ps[j][1]), i, j});
#         }
#     make_heap(begin(arr), end(arr), greater<array<int, 3>>());
#     while (!arr.empty()) {
#         pop_heap(begin(arr), end(arr), greater<array<int, 3>>());
#         auto [dist, i, j] = arr.back();
#         arr.pop_back();
#         i = find(ds, i), j = find(ds, j);
#         if (i != j) {
#             res += dist;
#             ds[i] += ds[j];
#             ds[j] = i;
#             if (ds[i] == -n)
#                 break;
#         }
#     }
#     return res;
# }

class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        n, q = len(a), []
        for i in range(n - 1):
            for j in range(i + 1, n):
                q.append((abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1]), i, j))
        UF = {i: i for i in range(n)}

        def union(u, v):
            UF[find(v)] = UF[find(u)]

        def find(u):
            if u != UF[u]:
                UF[u] = find(UF[u])
            return UF[u]
        heapify(q)
        ans, vis = 0, set()
        while q and len(set(find(u) for u in UF)) != 1:
            val, i, j = heappop(q)
            if find(i) != find(j):
                union(i, j)
                vis |= set([i, j])
                ans += val
                # print(ans, i, j, q)
        return ans
