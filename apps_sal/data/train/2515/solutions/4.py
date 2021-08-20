class Solution:

    def toGoatLatin(self, S: str) -> str:
        list_str = S.split(' ')
        s = ''
        for (index, word) in enumerate(list_str):
            if word[0].lower() in ('a', 'e', 'i', 'o', 'u'):
                s += ''.join('{word}ma{a} '.format(word=word, a='a' * (index + 1)))
            else:
                s += ''.join('{word}{alp}ma{a} '.format(word=word[1:], alp=word[0], a='a' * (index + 1)))
        return s.strip()
