def lottery(s):
    return ''.join(dict.fromkeys(filter(str.isdigit, s))) or 'One more run!'
