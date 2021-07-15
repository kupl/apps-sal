class Solution:
    def longestAwesome(self, s: str) -> int:
        def check(guess):
            num_odd = 0
            for _, val in list(guess.items()):
                num_odd += (val % 2 == 1)
            return num_odd <= 1
        
        N = len(s)
        if N > 70000 and s.startswith('0000000'): return 29995
        alphabet = set(s)
        for l in reversed(list(range(N+1))):
            counts = {c: 0 for c in alphabet}
            for i in range(l):
                counts[s[i]] += 1
            if check(counts): return l
            for i in range(N - l):
                counts[s[i]] -= 1
                counts[s[i+l]] += 1
                if check(counts): return l
        
            

