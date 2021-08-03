class Solution:
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        d = {}
        for a, b in zip(pattern, words):
            if a not in d:
                d[a] = b
            else:
                if d[a] != b:
                    return False

        values = list(d.values())
        return len(values) == len(set(values))
