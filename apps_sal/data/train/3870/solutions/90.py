def solve(s):
    spaces = [i for i in range(len(s)) if s[i] == ' ']
    letters = ''.join(x for x in s if x != ' ')[::-1]
    output = ''
    j = 0
    for i in range(len(s)):
        if i in spaces:
            output += ' '
        else:
            output += letters[j]
            j += 1
    return output
