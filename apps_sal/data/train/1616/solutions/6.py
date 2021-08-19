number_words = {'': 0, 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'one million': 1000000}


def parse_int(string):
    string_words = string.split()
    if 'thousand' in string_words:
        parts = string.partition('thousand')
        return parse_int(parts[0].strip()) * 1000 + parse_int(parts[2].strip())
    elif 'hundred' in string_words:
        parts = string.partition('hundred')
        return parse_int(parts[0].strip()) * 100 + parse_int(parts[2].strip())
    elif '-' in string:
        parts = string.replace('and ', '').split('-')
        return number_words[parts[0]] + number_words[parts[1]]
    else:
        return number_words[string.replace('and ', '')]
