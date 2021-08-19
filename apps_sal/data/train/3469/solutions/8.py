def count_consonants(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = []
    for letter in text:
        letter = letter.lower()
        conditions = [letter not in vowels, letter not in consonants, letter.isalpha()]
        if all(conditions):
            consonants.append(letter)
    return len(consonants)
