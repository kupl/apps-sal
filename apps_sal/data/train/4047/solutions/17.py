def to_leet_speak(str):
    leet = {'A': '@', 'B': '8', 'C': '(', 'E': '3', 'G': '6', 'H': '
    newstr = ''
    for c in str:
        if c in leet:
            newstr += leet[c]
        else:
            newstr += c
    return newstr
