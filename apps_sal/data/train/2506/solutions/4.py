class Solution:
    def isIsomorphic(self, s1, s2):
        # encode strings
        enc1, enc2 = [], []
        count1, count2 = 0, 0
        dict1, dict2 = dict(), dict()
        for i in range(len(s1)):
            char1, char2 = s1[i], s2[i]
            if char1 in dict1:
                enc1.append(dict1[char1])
            else:
                count1 += 1
                dict1[char1] = count1
                enc1.append(dict1[char1])
            if char2 in dict2:
                enc2.append(dict2[char2])
            else:
                count2 += 1
                dict2[char2] = count2
                enc2.append(dict2[char2])
        return enc1 == enc2  # compare encodings
