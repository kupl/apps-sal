class Solution:
    def findNextChar(self, string, i, char):
        otherChar = "R" if char == "L" else "L"
        for i in range(i, len(string)):
            if string[i] == otherChar:
                return None
            if string[i] == char:
                return i
        return None

    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        end_i = 0
        for i in range(len(start)):
            if start[i] != "X":
                end_i = self.findNextChar(end, end_i, start[i])
                if end_i == None or (start[i] == "L" and end_i > i) or (start[i] == "R" and end_i < i):
                    return False
                end_i += 1
        for end_i in range(end_i, len(end)):
            if end[end_i] != "X":
                return False

        return True
