def get_strings(city):
    city = city.replace(" ", "")
    characters = list((city).lower())
    char_dict = {}
    final = ""
    for char in characters:
        if char in char_dict.keys():
            char_dict[char] = char_dict[char] + "*"
        else: 
            char_dict[char] = char + ":*"
    for key in char_dict.values():
        final = final + (key + ",")
    return final[:-1]
