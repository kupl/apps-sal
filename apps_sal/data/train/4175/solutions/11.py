def repeater(string, n):
    string2 = string
    while len(string2) != len(string) * n:
        string2 += string
    return string2
