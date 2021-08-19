class Solution:

    def sortString(self, s: str) -> str:
        ss = sorted(list(dict.fromkeys(s)))
        ssr = ss + ss[::-1]
        dic = {}
        final_s = ''
        for i in ss:
            dic[i] = 0
        for i in s:
            dic[i] += 1
        for i in range(len(s)):
            for j in ssr:
                if dic[j] > 0:
                    final_s += j
                    dic[j] -= 1
        return final_s
