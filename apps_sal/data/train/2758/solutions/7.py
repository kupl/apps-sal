def decode(number):
    foo = str(number).split('98')
    parts = foo[:-1] if foo[-1] == '' else foo
    output = ""
    for i in range(len(parts)):
        if i % 2 == 0:
            for x in range(0, len(parts[i]), 3):
                output += chr(int(parts[i][x:x+3])-4)
            output += ', '
        else:
            output += str(int(parts[i], 2))
            if i != len(parts)-1:
                output += ', '
    return output
    

