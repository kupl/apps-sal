def solve(s):
    letters = [l for l in s]
    spaces = [idx for (idx, space) in enumerate(s) if space == ' ']
    reverse_letters = []
    for (i, j) in enumerate(letters):
        reverse_letters.append(letters[-1 - i])
    reverse_letters = [l for l in reverse_letters if l != ' ']
    for (idx, j) in enumerate(spaces):
        reverse_letters.insert(j, ' ')
    return ''.join(reverse_letters)
