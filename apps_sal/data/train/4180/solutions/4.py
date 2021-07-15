def lottery(s):
    return ''.join({i:1 for i in s if i.isdigit()}) or 'One more run!'
