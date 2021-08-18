def to_leet_speak(str):
    ans = ''
    alp = {'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': '
    for i in str:
        ans = ans + alp.get(i, ' ')

    return ans
