class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        A = []
        for i in range(len(words)):
            A.append(len(words[i]))
        temp = 0
        k = 0
        B = []
        for i in range(len(A)):
            if temp == 0:
                temp = A[i]
            elif (temp + 1 + A[i]) > maxWidth:
                if i - k == 1:
                    B.append([k, i, 0, 0])
                else:
                    B.append([k, i, (maxWidth - temp + i - k - 1) // (i - k - 1), (maxWidth - temp + i - k - 1) % (i - k - 1)])
                temp = A[i]
                k = i
            else:
                temp = temp + 1 + A[i]
            if i == len(A) - 1:
                B.append([k, i + 1, 1, 0])
        str1 = ''
        ans = []
        for i in range(len(B)):
            for j in range(B[i][0], B[i][1]):
                if j == B[i][0]:
                    str1 += words[B[i][0]]
                elif B[i][3]:
                    str1 = str1 + (B[i][2] + 1) * ' ' + words[j]
                    B[i][3] -= 1
                else:
                    str1 = str1 + B[i][2] * ' ' + words[j]
            if i == len(B) - 1 or B[i][1] - B[i][0] == 1:
                str1 = str1 + (maxWidth - len(str1)) * ' '
            ans.append(str1)
            str1 = ''
        return ans
