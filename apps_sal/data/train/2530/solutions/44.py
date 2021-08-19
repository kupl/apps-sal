class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        table = defaultdict(int)
        c = 0
        for i, t in enumerate(time):
            # print(60-(t%60))
            # print(table)
            if 60 - (t % 60) in table:
                c += table[60 - (t % 60)]
            # else:
            if t % 60 == 0:
                table[60] += 1
            else:
                table[(t % 60)] += 1
        # print(table)
        return c
