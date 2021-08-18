def get_strings(city):
    new_city = ''.join(filter(str.isalpha, city.lower()))

    char_seen = []
    for char in new_city:
        if char not in char_seen:
            char_seen.append(char)

    count_char = []
    for char in char_seen:
        x = new_city.count(char)
        count_char.append(x)

    d = dict(zip(char_seen, count_char))

    total_str = ""
    for char, count in d.items():
        total_str += char + ":" + count * "*" + ","

    return total_str[:-1]
