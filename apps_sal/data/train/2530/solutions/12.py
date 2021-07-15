class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash_table = defaultdict(int)
        x = 0
        for i in time:
            if (60-(i%60))%60 in hash_table:
                x += hash_table[(60-(i%60))%60]
            hash_table[(i%60)] += 1
        print(hash_table)
        return x

