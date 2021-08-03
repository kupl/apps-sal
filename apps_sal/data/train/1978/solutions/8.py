class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(list1, pattern):
            for i in range(len(pattern)):
                if list1[i] != pattern[i]:
                    return False
            return True

        def number_arr(list1):
            dict = {}
            arr = []
            last_given_value = 0
            for i in list1:
                if i not in dict:
                    last_given_value += 1
                    dict[i] = last_given_value
                    arr.append(dict[i])
                else:
                    arr.append(dict[i])
            return arr

        pat = number_arr(pattern)
        ans = []
        for word in words:
            word_list = number_arr(word)
            if match(pat, word_list):
                ans.append(word)
        return ans
