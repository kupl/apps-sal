class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        block = False
        res = []
        buffer = ''
        for line in source:
            i = 0
            while i < len(line):
                if line[i] == '/' and i < len(line) - 1 and line[i + 1] == '/' and not block:
                    i = len(line)
                elif line[i] == '/' and i < len(line) - 1 and line[i + 1] == '*' and not block:
                    i += 2
                    block = True
                elif line[i] == '*' and i < len(line) - 1 and line[i + 1] == '/' and block:
                    i += 2
                    block = False
                else:
                    if not block:
                        buffer += line[i]
                    i += 1
            if buffer and not block:
                res.append(buffer)
                buffer = ''
        return res
