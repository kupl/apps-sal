def remove(s):
    num_of_marks = 0
    while s[-num_of_marks - 1] == '!':
        num_of_marks += 1
    s = s.replace('!', '')
    return s + '!' * num_of_marks
