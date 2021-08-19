def execute(code):
    path = translatePath(createPath(transformCode(removeBrackets(code))))
    if path == '':
        return '*'
    xmax = 0
    ymax = 0
    for coordinate in path:
        if coordinate[0] > xmax:
            xmax = coordinate[0]
        if coordinate[1] > ymax:
            ymax = coordinate[1]
    grid = []
    for something in range(ymax + 1):
        grid.append((xmax + 1) * [' '])
    for visited in path:
        grid[visited[1]][visited[0]] = '*'
    finalstring = ''
    for row in grid:
        for elem in row:
            finalstring += elem
        finalstring += '\r\n'
    return finalstring[:-2]


def removeBrackets(rscommand):
    if rscommand.find('(') == -1:
        return rscommand
    found = False
    indeks = 0
    openbracketindex = 0
    closingbracketindex = 0
    while not found and indeks < len(rscommand):
        if rscommand[indeks] == '(':
            openbracketindex = indeks
        if rscommand[indeks] == ')':
            closingbracketindex = indeks
            found = True
        indeks += 1
    leftpart = rscommand[:openbracketindex]
    rightpart = rscommand[closingbracketindex + 1:]
    middlepart = rscommand[openbracketindex + 1:closingbracketindex]
    factor = ''
    indeks = 0
    if len(rightpart) > 0:
        while rightpart[indeks].isdigit():
            factor += rightpart[indeks]
            indeks += 1
            if indeks == len(rightpart):
                break
    if indeks > 0:
        newcommand = leftpart + int(factor) * middlepart + rightpart[indeks:]
    else:
        newcommand = leftpart + middlepart + rightpart
    return removeBrackets(newcommand)


def createPath(command):
    state = [0, 0, 'E']
    path = [[0, 0]]
    for x in command:
        if x == 'L' or x == 'R':
            state = makeTurn(state, x)
        else:
            state = moveForward(state)
            path.append([state[0], state[1]])
    return path


def translatePath(path):
    minx = 0
    miny = 0
    for c in path:
        if c[0] < minx:
            minx = c[0]
        if c[1] < miny:
            miny = c[1]
    for c in path:
        c[0] = c[0] - minx
        c[1] = c[1] - miny
    return path


def moveForward(state):
    if state[2] == 'N':
        return [state[0], state[1] - 1, state[2]]
    if state[2] == 'S':
        return [state[0], state[1] + 1, state[2]]
    if state[2] == 'W':
        return [state[0] - 1, state[1], state[2]]
    return [state[0] + 1, state[1], state[2]]


def makeTurn(state, leftorright):
    if leftorright == 'L':
        if state[2] == 'N':
            return [state[0], state[1], 'W']
        if state[2] == 'W':
            return [state[0], state[1], 'S']
        if state[2] == 'S':
            return [state[0], state[1], 'E']
        if state[2] == 'E':
            return [state[0], state[1], 'N']
    if leftorright == 'R':
        if state[2] == 'N':
            return [state[0], state[1], 'E']
        if state[2] == 'W':
            return [state[0], state[1], 'N']
        if state[2] == 'S':
            return [state[0], state[1], 'W']
        if state[2] == 'E':
            return [state[0], state[1], 'S']


def transformCode(code):
    newcode = ''
    indeks = 0
    while indeks < len(code):
        while not code[indeks].isdigit():
            newcode += code[indeks]
            indeks += 1
            if indeks == len(code):
                break
        if indeks == len(code):
            break
        factor = ''
        while code[indeks].isdigit():
            factor += code[indeks]
            indeks += 1
            if indeks == len(code):
                break
        newcode = newcode[:-1] + int(factor) * newcode[-1]
    return newcode
