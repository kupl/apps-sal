class Solution:

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        (start, end) = (0, len(s) - 1)
        lists = list(s)
        while start < end:
            if lists[start] in vowel:
                while lists[end] not in vowel:
                    end -= 1
                if end < start:
                    break
                temp = lists[start]
                lists[start] = lists[end]
                lists[end] = temp
                start += 1
                end -= 1
            else:
                start += 1
        return ''.join(lists)
