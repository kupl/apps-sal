def is_haiku(text):
    """
    Given lines of text, determines if those lines constitute a haiku
    """
    syllables_per_line = []
    lines = text.splitlines()
    for i in range(len(lines)):
        line = lines[i].split(" ")
        syllables = 0
        for word in line:
            syllables += count_syllables(word)
        syllables_per_line.append(syllables)
    if syllables_per_line == [5, 7, 5]:
        return True
    else:
        return False
        

def count_syllables(word):
    """
    Given a word, count the number of syllables
    """
    syllables_in_word = 0
    vowels = 'aeiouy'
    word = "".join(filter(str.isalnum, word))
    word = word.lower()
    if len(word) > 0:
        if word[0] in vowels:
            syllables_in_word = 1
        if len(word) > 1:
            i = 0
            # count consonant, vowel pairs
            while i < len(word)-1:
                if (word[i] not in vowels) & (word[i+1] in vowels):
                    syllables_in_word += 1
                    i += 1
                i += 1
            # take care of silent 'e'
            # last part of if for double vowel word endings: ex. pursue, levee
            if (syllables_in_word > 1) & (word.endswith('e')) & (word[len(word)-2] not in vowels):
                syllables_in_word -= 1
    # print(f"word: {word}, syllables: {syllables_in_word}")
    return syllables_in_word
