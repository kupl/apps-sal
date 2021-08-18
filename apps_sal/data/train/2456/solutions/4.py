class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        s = []

        for i in S:
            if i == '
            if s:
                s.pop()

            else:
                s.append(i)

        t = []

        for i in T:
            if i == '
            if t:
                t.pop()

            else:
                t.append(i)

        if s == t:
            return True

        return False
