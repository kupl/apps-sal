def to_leet_speak(str):
    LeetSpeak = {'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': '
    return ''.join(LeetSpeak[x] if x in LeetSpeak else x for x in str)
