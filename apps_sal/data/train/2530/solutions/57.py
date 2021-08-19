class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash_map = {}
        ans = 0
        for t in time:
            rem = t % 60
            key = 60 - rem
            if key in hash_map:
                ans += len(hash_map[key])
            hash_map[rem] = hash_map.get(rem, []) + [t]
            if rem == 0:
                hash_map[key] = hash_map.get(key, []) + [t]
        return ans
