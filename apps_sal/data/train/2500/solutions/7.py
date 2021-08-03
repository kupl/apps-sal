class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        last_char = s[0]
        count = 1
        max_count = 0
        for c in s[1:]:
            if c == last_char:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1

            last_char = c
        if count > max_count:
            max_count = count

        return max_count
