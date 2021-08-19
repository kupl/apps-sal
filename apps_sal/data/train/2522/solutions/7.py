class Solution:
    def countAndSay(self, n):
        s = [['1']]
        for i in range(n):  # 某一个子串
            str1 = s[i]
            temp = []
            # for j in range(len(str1)): # 某一个新字符
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

        # res = 0
        # for t in s[n-1]:
        #     res = res * 10 + int(t)

        res = [''.join(s[n - 1])]

        return res[0]
