class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # d['a'] = word
        #pattern_arr = list(pattern)
        str_arr = str.split()
        pattern_dict = {}
        str_dict = {}

        pattern_tokenize = []
        token_p = 0

        str_tokenize = []
        token_s = 0

        for char in pattern:
            if char not in list(pattern_dict.keys()):
                pattern_dict[char] = token_p
                token_p += 1
                pattern_tokenize.append(token_p)
            else:
                pattern_tokenize.append(pattern_dict[char])

        for word in str_arr:
            if word not in list(str_dict.keys()):
                str_dict[word] = token_s
                token_s += 1
                str_tokenize.append(token_s)
            else:
                str_tokenize.append(str_dict[word])

        return (pattern_tokenize == str_tokenize)
