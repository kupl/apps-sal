from string import ascii_lowercase as al
tbl = str.maketrans(al, ''.join((al[(i - 1) % 26] if x in 'aeiou' else next((al[j % 26] for j in range(i + 1, 100) if al[j % 26] in 'aeiou')) for (i, x) in enumerate(al))))


def replace_letters(word):
    return word.translate(tbl)
