class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"

        seq = self.countAndSay(n - 1)

        seq2 = ""
        count = 0

        for i in range(len(seq)):
            num = seq[i]
            count += 1
            if i == len(seq) - 1:
                seq2 = seq2 + str(count) + num
            elif seq[i + 1] != seq[i]:
                seq2 = seq2 + str(count) + num
                count = 0  # reset count

        return seq2
