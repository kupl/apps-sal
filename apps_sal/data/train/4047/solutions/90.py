def to_leet_speak(str):
    leet_dict = {' ': ' ', 'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': '
    leet_list = []
    for i in str:
        if i in leet_dict.keys():
            leet_list.append(leet_dict.get(i))
    return ''.join(leet_list)
