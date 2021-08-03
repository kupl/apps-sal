class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        c = 0
        i = 0
        while i < len(logs):
            if logs[i] == '../':
                if c != 0:
                    c -= 1
            elif logs[i] == './':
                i += 1
                continue
            else:
                c += 1
            i += 1
        return c
