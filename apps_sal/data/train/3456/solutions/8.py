def repeater(string, n):
    longString = ''
    for i in range(n):
        longString += string
    return '"' + string + '" repeated ' + str(n) + ' times is: "' + longString + '"'
