def presses(phrase):
    x = 0
    for letter in phrase:
        if letter.lower() in list('1*#adgjmptw '):
            x += 1
        elif letter.lower() in list('0behknqux'):
            x += 2
        elif letter.lower() in list('cfilorvy'):
            x += 3
        elif letter.lower() in list('234568sz'):
            x += 4
        elif letter.lower() in list('79'):
            x += 5
    return x
