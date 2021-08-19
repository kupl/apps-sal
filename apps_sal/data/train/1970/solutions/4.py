class Solution:
    def getPalindromic(self, num, mid=''):
        return str(num) + mid + str(num)[::-1]

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if len(n) == 1:
            return str(int(n) - 1)
        midstr = '' if len(n) % 2 == 0 else n[len(n) // 2]
        midint = -1 if len(n) % 2 == 0 else int(n[len(n) // 2])
        s = [''] * 6
        # 99..99
        s[0] = '9' * (len(n) - 1)
        # (l-1)m(l-1)
        s[1] = self.getPalindromic(int(n[:(len(n)) // 2]) - 1, midstr)
        # l(m-1)l
        s[2] = n[:len(n) // 2] + str(midint - 1) + n[:len(n) // 2][::-1] if midint > 0 else self.getPalindromic(int(n[:len(n) // 2]) - 1)
        # lml
        s[3] = n[:len(n) // 2] + midstr + n[:len(n) // 2][::-1]
        # l(m+1)l
        s[4] = n[:len(n) // 2] + str(midint + 1) + n[:len(n) // 2][::-1] if midint < 10 and midint > -1 else self.getPalindromic(int(n[:len(n) // 2]) + 1)
        # 10..01
        s[5] = '1' + '0' * (len(n) - 1) + '1'
        nums = map(lambda x: abs(int(x) - int(n)), s)
        nums = list(map(lambda x: x if x > 0 else 1e18, nums))
        return s[nums.index(min(nums))]
