def to_leet_speak(str):
    return (lambda base: ''.join([base[l] if l in base else l for l in str]))({'A': '@', 'B': '8', 'C': '(', 'E': '3', 'G': '6', 'H': '#', 'I': '!', 'L': '1', 'O': '0', 'S': '$', 'T': '7', 'Z': '2'})
