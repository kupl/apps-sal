class Solution:

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        wordlist = str.split()
        dictionary = {}
        L1 = len(pattern)
        L2 = len(wordlist)
        if L1 != L2:
            return False
        else:
            for n in range(L1):
                if pattern[n] in dictionary.keys():
                    if dictionary[pattern[n]] != wordlist[n]:
                        return False
                elif wordlist[n] not in dictionary.values():
                    dictionary[pattern[n]] = wordlist[n]
                else:
                    return False
        return True
