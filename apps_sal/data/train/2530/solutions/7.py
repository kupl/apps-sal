class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        mods = {}
        for (i, v) in enumerate(time):
            rem = v % 60
            needed_rem = (60 - rem) % 60
            if needed_rem in mods:
                count += len(mods[needed_rem])
            if rem in mods:
                mods[rem].append(v)
            else:
                mods[rem] = [v]
        return count
