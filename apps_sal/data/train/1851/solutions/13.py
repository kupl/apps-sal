import math

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        longest = sorted(clips, key=lambda a: a[1])[-1][1]
        memo = [[None for i in range(longest + 1)] for i in range(len(clips))]
        
        def dp(i, start):
            if start >= T:
                return 0
            
            curr = clips[i]
            if curr[0] > start:
                return math.inf
            elif i == len(clips) - 1:
                if curr[1] < T:
                    return math.inf
                return 1
            
            # Pick first clip
            if memo[i + 1][curr[1]] == None:
                memo[i + 1][curr[1]] = dp(i + 1, curr[1])
            
            #Don't pick first clip
            if memo[i + 1][start] == None:
                memo[i + 1][start] = dp(i + 1, start)
            
            return min(1 + memo[i + 1][curr[1]], memo[i + 1][start])
        
        res = dp(0, 0)
        return res if res != math.inf else -1
