class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = set()
        for i in range(ord('a'), ord('z') + 1):
            s.add(chr(i))
        for i in range(ord('A'), ord('Z') + 1):
            s.add(chr(i))
        order = []
        for i in range(len(S)):
            if S[i] in s:
                order.append(S[i])
        new = []
        order.reverse()
        for i in reversed((S)):
            if i in s:
                new.append(order.pop())
            else:
                new.append(i)
        return ''.join(reversed(new))
