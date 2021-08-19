class Solution:

    def removeDuplicates(self, S: str) -> str:
        prev = S
        while True:
            i = 0
            s = ''
            while i < len(prev):
                if i != len(prev) - 1 and prev[i] == prev[i + 1]:
                    i += 2
                else:
                    s += prev[i]
                    i += 1
            if prev == s:
                break
            prev = s
        return s
