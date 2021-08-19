letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def reverse_letter(string):
    string = string[::-1]
    returner = []
    for item in string:
        if item in letters:
            returner.append(item)
    return ''.join(returner)
