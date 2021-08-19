def to_leet_speak(str):
    leet = {'A': '@', 'B': '8', 'C': '(', 'E': '3', 'G': '6', 'H': '#', 'I': '!', 'L': '1', 'O': '0', 'S': '$', 'T': '7', 'Z': '2'}
    newstr = ''
    for c in str:
        if c in leet:
            newstr += leet[c]
        else:
            newstr += c
    return newstr
