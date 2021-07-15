class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mem = defaultdict(int)
        count = 0
        
        for t in time:
            t = t%60
            target = (60-t)%60
            print(t, target)
            count = count+mem[target]
            mem[t] += 1
        print(mem, count)
        return count
