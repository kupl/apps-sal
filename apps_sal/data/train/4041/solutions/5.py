def sort_my_string(s):
    odd, even = [], []
    for i, char in enumerate(s):
        even.append(char) if i % 2 == 0 else odd.append(char)
    return "".join(even) + " " + "".join(odd)
