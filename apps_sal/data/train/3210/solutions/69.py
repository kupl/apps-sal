def get_strings(city):
    city = city.lower()
    return ','.join((f"{letter}:{count * '*'}" for (letter, count) in {letter: city.count(letter) for letter in city if not letter.isspace()}.items()))
