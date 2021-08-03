def get_strings(city):
    # create lower_case city only with letters
    new_city = ''.join(filter(str.isalpha, city.lower()))

    # list of unique letters
    char_seen = []
    for char in new_city:
        if char not in char_seen:
            char_seen.append(char)

    # list of counts for unique letters
    count_char = []
    for char in char_seen:
        x = new_city.count(char)
        count_char.append(x)

    # create dictionary with two parallel list
    d = dict(zip(char_seen, count_char))

    total_str = ""
    for char, count in d.items():
        total_str += char + ":" + count * "*" + ","  # using += to append instead

    return total_str[:-1]
