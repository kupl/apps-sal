def get_strings(city):
    letters = {}
    for letter in city.lower():
        if letter in letters:
            value = letters[letter]
            value += 1
            letters.update({letter: value})
        else:
            letters.update({letter: 1})
    result = ""
    for letter in city.lower().replace(" ", ""):
        if letter not in result:
            result += letter + ':' + '*' * letters[letter] + ','
    return result[:-1]
