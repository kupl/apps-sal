def reverse_in_parentheses(string):
    a = 0
    for n in range(string.count('(')):
        (a, b) = (string.find('(', a), 0)
        for i in range(a, len(string)):
            if string[i] == '(':
                b += 1
            elif string[i] == ')':
                b -= 1
            if b == 0:
                break
        a += 1
        string = string[:a] + string[a:i][::-1].translate(str.maketrans(')(', '()')) + string[i:]
    return string
