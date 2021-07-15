def vowel_2_index(str_to_switch):
    result = ""
    vowels = "aeiouAEIOU"
    for index, ch in enumerate(str_to_switch):
        if ch in vowels:
            result += str(index+1)
        else:
            result += ch
    return result
