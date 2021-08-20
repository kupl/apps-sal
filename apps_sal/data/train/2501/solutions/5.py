class Solution:

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        output_chars = list()
        num_segments = len(s) // k + 1
        for j in range(num_segments):
            start = 2 * j * k
            end = 2 * (j + 1) * k
            reverse_up_to = min(start + k, len(s))
            seg = min(start + 2 * k, len(s))
            for i in range(reverse_up_to - 1, start - 1, -1):
                output_chars.append(s[i])
            for i in range(reverse_up_to, seg):
                output_chars.append(s[i])
        return ''.join(output_chars)
