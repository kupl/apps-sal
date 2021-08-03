class Solution:

    def __init__(self):
        self.seen = {0: -1}
        self.len = 0

    def update_best_length(self, num, p):
        if num in self.seen:
            self.len = max(self.len, p - self.seen[num])

        for i in range(10):
            x = num ^ (1 << int(i))
            if x in self.seen:
                self.len = max(self.len, p - self.seen[x])

    def longestAwesome(self, s: str) -> int:
        num = 0
        for p, c in enumerate(s):
            num = num ^ (1 << int(c))
            self.update_best_length(num, p)
            if num not in self.seen:
                self.seen[num] = p

        return self.len
