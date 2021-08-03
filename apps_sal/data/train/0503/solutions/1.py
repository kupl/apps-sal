class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        words = []
        word = ''
        word_len = 0
        for char in text:
            if char == ' ':
                words.append((word_len, word))
                word = ''
                word_len = 0
            else:
                word += char
                word_len += 1
        if (word_len > 0):
            words.append((word_len, word))
        words.sort(key=lambda tup: tup[0])
        output = ''
        for word in words:
            output += word[1] + ' '
        return output[:-1].capitalize()
