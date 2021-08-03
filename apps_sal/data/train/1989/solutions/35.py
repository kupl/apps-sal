class Solution:
    def longestAwesome(self, s: str) -> int:
        pattern = [1 << i for i in range(10)]

        seen, state = {}, 0
        seen[state] = -1

        answer = 0
        for i, c in enumerate(s):
            state ^= 1 << int(c)
            if state in seen:
                answer = max(answer, i - seen[state])
            for p in pattern:
                target = state ^ p
                if target in seen:
                    answer = max(answer, i - seen[target])

            if state not in seen:
                seen[state] = i

        return answer
