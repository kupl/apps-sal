from string import ascii_lowercase as alpha

alpha = list(alpha)
ln = len(alpha)
vowels = "aeiou"


def vowel_back(s):
    s = list(s)
    for idx, char in enumerate(s):
        index = alpha.index(char)
        if char in ('c', 'o'):
            s[idx] = alpha[index - 1]
        elif char == 'd':
            s[idx] = alpha[index - 3]
        elif char == 'e':
            s[idx] = alpha[index - 4]
        else:
            if char in vowels:
                s[idx] = alpha[index - 5]
            else:
                index += 9
                index = index % ln
                s[idx] = alpha[index]
        if s[idx] in ('c', 'o', 'd', 'e'):
            s[idx] = char
    return "".join(s)
