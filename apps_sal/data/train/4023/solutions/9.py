from string import ascii_lowercase

def high(x):
    letter_worth = {letter: int(index) for index, letter in enumerate(ascii_lowercase, start=1)}
    words = x.split()
    total = []
    for word in words:
        count = 0
        for letter in word:
            count += letter_worth.get(letter)
        total.append(count)
    return words[total.index(max(total))]
