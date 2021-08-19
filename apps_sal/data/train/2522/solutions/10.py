class Solution:

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return 0
        else:
            s = '1'
            for i in range(n - 1):
                res = ''
                k = 0
                m = len(s)
                count = 1
                while k < m:
                    say = s[k]
                    if k + 1 < m:
                        if s[k] == s[k + 1]:
                            count += 1
                            k += 1
                        else:
                            res += str(count)
                            res += say
                            count = 1
                            k += 1
                    else:
                        res += str(count)
                        res += say
                        break
                s = res
            return s
