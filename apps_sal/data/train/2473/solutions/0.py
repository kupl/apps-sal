class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) == 0:
            return s
        string = ['#']
        string.extend(list(s))
        string.append('#')
        for i in range(1, len(string) - 1):
            if string[i] == '?':
                for j in range(97, 123):
                    if string[i - 1] != chr(j) and string[i + 1] != chr(j):
                        string[i] = chr(j)
                        break

        ret = ''.join(string[1:-1])
        return ret
