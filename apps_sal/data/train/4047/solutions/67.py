def to_leet_speak(str):
    LeetSpeak = {'A': '@', 'B': '8', 'C': '(', 'E': '3', 'G': '6', 'H': '
    return ''.join(LeetSpeak[x] if x in LeetSpeak else x for x in str)
