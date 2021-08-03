def sort_word(word):
    characters = [[], []]
    for char in word:
        characters[char.isalpha()].append(char)
    characters[1] = characters[1][:len(word) > 1] + sorted(characters[1][1:-1]) + characters[1][-1:]
    return ''.join(characters[char.isalpha()].pop() for char in reversed(word))[::-1]


def scramble_words(words):
    return ' '.join(map(sort_word, words.split()))
