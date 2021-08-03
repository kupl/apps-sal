class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        take = [False] * N
        MOD = 10**9 + 7

        fenwick = [0] * (N + 1)

        def add(idx, val):
            idx += 1  # Make 1 based index
            while idx <= N:
                fenwick[idx] += val
                idx += idx & -idx

        def sum_(idx):
            idx += 1  # Make 1 based index
            ans = 0

            while idx > 0:
                ans += fenwick[idx]
                idx -= idx & -idx
            return ans

        def range_sum(a, b):
            return sum_(b) - sum_(a - 1)

        for a, b in requests:
            # Make one based index
            add(a, 1)
            add(b + 1, -1)

        occurrences = [0] * N

        for i in range(N):
            occurrences[i] = sum_(i)

        occ = sorted([(v, i) for i, v in enumerate(occurrences)], reverse=True)
        nums.sort()

        ans = 0
        for a, b in occ:
            if a:
                ans += (nums.pop() * a)

        return ans % MOD


#         vector<int> bit;  // binary indexed tree
#     int n;

#     FenwickTreeOneBasedIndexing(int n) {
#         this->n = n + 1;
#         bit.assign(n + 1, 0);
#     }

#     FenwickTreeOneBasedIndexing(vector<int> a)
#         : FenwickTreeOneBasedIndexing(a.size()) {
#         for (size_t i = 0; i < a.size(); i++)
#             add(i, a[i]);
#     }

#     int sum(int idx) {
#         int ret = 0;
#         for (++idx; idx > 0; idx -= idx & -idx)
#             ret += bit[idx];
#         return ret;
#     }

#     int sum(int l, int r) {
#         return sum(r) - sum(l - 1);
#     }

#     void add(int idx, int delta) {
#         for (++idx; idx < n; idx += idx & -idx)
#             bit[idx] += delta;
#     }
