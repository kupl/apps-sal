class Solution:
    def reorderSpaces(self, text: str) -> str:
        # count the number of space
        cnt_space = 0
        cnt_words = 0
        for i in range(len(text)):
            if text[i] == ' ':
                cnt_space += 1
            elif cnt_words == 0 or text[i - 1] == ' ':
                cnt_words += 1
        # calculate extra space nad calculate avg space
        extra_space = 0
        avg_space = 0
        if cnt_words < 2:
            extra_space = cnt_space
        else:
            extra_space = cnt_space % (cnt_words - 1)
            avg_space = cnt_space // (cnt_words - 1)
        
        #
        result = ''
        word_appeared = False
        for i in range(len(text)):
            if text[i] != ' ':
                if word_appeared and text[i - 1] == ' ':
                    result += ' ' * avg_space
                word_appeared = True
                result += text[i]
                
                
        result += ' ' * extra_space
        return result
