def to_leet_speak(str):
    leet = {'A': '@', 'B': '8', 'C': '(', 'E': '3', 'G': '6', 'H': '
    return "".join([leet[letter] if letter in leet.keys() else letter for letter in str])
