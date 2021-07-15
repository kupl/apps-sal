class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        memo = defaultdict(int)
        for t in text:
            if t in 'balon':
                memo[t] += 1
        count_once = min(memo['b'], memo['a'], memo['n'])
        count_twice = min(memo['l'], memo['o'])
        return min(count_once, count_twice // 2)
