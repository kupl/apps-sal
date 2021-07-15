def solve(s):
    lst = [i for i in s if i != ' ']
    return ''.join(' ' if i == ' ' else lst.pop() for i in s)
