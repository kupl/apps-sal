def solve(s):
    lst = [i for i in s[::-1] if i != ' ']
    
    for i in range(len(s)):
        if s[i] == ' ':
            lst.insert(i, ' ')

    return ''.join(lst)
