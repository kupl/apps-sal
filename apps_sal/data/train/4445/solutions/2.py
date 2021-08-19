import re


def is_haiku(text):

    def parse_line(line):
        word_pattern = '[^\\W\\d_]+'
        return re.findall(word_pattern, line)

    def count_syllables(word):
        vowel_pattern = '[aeiouy]+'
        vowels = re.findall(vowel_pattern, word, re.I)

        def ends_in_e(seq):
            return seq[-1] == 'e'
        if vowels and ends_in_e(vowels) and ends_in_e(word):
            vowels.pop()
        return max(len(vowels), 1)
    syllables = [sum(map(count_syllables, parse_line(line))) for line in text.splitlines()]
    return syllables == [5, 7, 5]
