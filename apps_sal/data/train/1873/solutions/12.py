class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        def countX(s, char='R'):
            if char == 'L':
                s = s[::-1]
            countX = 0
            ans = []
            for c in s:
                if c == char:
                    ans.append(countX)
                elif c == 'X':
                    countX += 1
            return ans

        startLR = "".join(c for c in start if c != 'X')
        endLR = "".join(c for c in end if c != 'X')
        startR, startL = countX(start, 'R'), countX(start, 'L')
        endR, endL = countX(end, 'R'), countX(end, 'L')

        return (startLR == endLR) and \
            all([startR[i] <= endR[i] for i in range(len(startR))]) and \
            all([startL[i] <= endL[i] for i in range(len(startL))])
