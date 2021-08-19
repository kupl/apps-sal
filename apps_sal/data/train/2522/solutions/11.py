class Solution:

    def countAndSay(self, n):
        """
        not mine!
        """
        s = '1'
        for _ in range(n - 1):
            s = re.sub('(.)\\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s
