from re import findall

def duplicate_count(text):
    return (len(findall("(\w)\\1+", "".join(sorted(text.upper())))))

