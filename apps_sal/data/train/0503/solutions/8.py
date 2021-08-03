class Solution:
    def arrangeWords(self, text: str) -> str:
        if not text:
            return text

        words = text.lower().split(' ')

        words = sorted(words, key=lambda x: len(x))
        words[0] = words[0][0].upper() + words[0][1:]

        return ' '.join(words)
