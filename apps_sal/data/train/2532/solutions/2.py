class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        arr = []
        for i, c in enumerate(reversed(s)):
            if i and not i % 3:
                arr.append('.')
            arr.append(c)
        return ''.join(reversed(arr))
