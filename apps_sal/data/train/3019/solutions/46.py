def str_count(strng, letter):
    letter_count = {letter: 0}
    for char in strng:
        if char == letter:
            letter_count[char] += 1
    return letter_count[letter]
