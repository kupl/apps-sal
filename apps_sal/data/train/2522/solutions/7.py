class Solution:

    def countAndSay(self, n):
        s = [['1']]
        for i in range(n):
            str1 = s[i]
            temp = []
            j = 0
            while j < len(str1):
                count = 1
                while j <= len(str1) - 2 and str1[j] == str1[j + 1]:
                    count += 1
                    j += 1
                temp.append(str(count))
                temp.append(str1[j])
                j += 1
            s.append(temp)
        res = [''.join(s[n - 1])]
        return res[0]
