def to_leet_speak(str):
    x = {'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': '
    y = ""
    for i in str:
        try:
            y += x[i]
        except:
            y += i
    return y
