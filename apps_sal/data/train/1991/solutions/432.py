# https://leetcode.com/problems/count-all-possible-routes/discuss/843602/Java-or-DP-all-approaches --> another dp solution
# public long countRoutesApproach3(int start, int[] locations, int finish, int fuel) {
# \tint len = locations.length;
# \tlong res = 0;
# \tmemo = new long[len][fuel + 1];

# \tmemo[start][0] = 1;

# \tfor (int fuelLeft = 1; fuelLeft <= fuel; fuelLeft++) {

# \t\tfor (int j = 0; j < len; j++) {
# \t\t\tfor (int k = 0; k < len; k++) {

# \t\t\t\t// Visit all cities except `curCity`
# \t\t\t\tif (k == j) {
# \t\t\t\t\tcontinue;
# \t\t\t\t}

# \t\t\t\tint fuelNeeded = Math.abs(locations[j] - locations[k]);
# \t\t\t\tif (fuelNeeded <= fuelLeft) { // we still have fuel left
# \t\t\t\t\tmemo[j][fuelLeft] = (memo[j][fuelLeft] + memo[k][fuelLeft - fuelNeeded]) % range;
# \t\t\t\t}
# \t\t\t}
# \t\t}

# \t\tres = (res + memo[finish][fuelLeft]) % range;
# \t}

# \treturn res;
# }
class Solution:
    def countRoutes(self, a: List[int], s: int, e: int, f: int) -> int:
        ans, n = 0, len(a)
        dp = [[0]*(f+1) for _ in range(n)]
        dp[s][0] = 1
        for ff in range(f+1):
            for i in range(n):
                for k in range(n):
                    if i != k:
                        dist = abs(a[i] - a[k])
                        if dist <= ff: dp[i][ff] += dp[k][ff-dist]
            ans += dp[e][ff]
        return ans % (10**9+7)
