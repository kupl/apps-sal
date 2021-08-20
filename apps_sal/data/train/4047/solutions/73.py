leet_dict = {'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': '#', 'I': '!', 'J': 'J', 'K': 'K', 'L': '1', 'M': 'M', 'N': 'N', 'O': '0', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': '$', 'T': '7', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '2'}


def to_leet_speak(str):
    leet_phrase = ''
    for x in str:
        if x == ' ':
            leet_phrase += x
        else:
            leet_phrase += leet_dict.get(x.upper())
    return leet_phrase
