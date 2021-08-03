def remove_parentheses(s):
    s2 = s.replace('(', '|').replace(')', '|')
    level = 0
    start = 0
    i = s2.find('|')
    while i != -1:
        if s[i] == '(':
            if (level == 0):
                start = i
            level += 1
        elif s[i] == ')':
            level -= 1
            if (level == 0):
                s = s[0:start] + s[i + 1:]
                s2 = s2[0:start] + s2[i + 1:]
                i = -1
        i = s2.find('|', i + 1)
    return s


print((remove_parentheses("example(unwanted thing)example")))
