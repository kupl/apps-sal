def longest(s1, s2):
    letters_count = [0] * 26
    for letter in s1:
        letters_count[ord(letter) - 97] += 1
    for letter in s2:
        letters_count[ord(letter) - 97] += 1
    result = []
    for i in range(26):
        if letters_count[i] > 0:
            result.append(chr(i + 97))
    return ''.join(result)
