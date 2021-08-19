import re


def solve(*eqs):
    # put all equations in list of dictionaries
    sysofeq = []
    for x in eqs:
        # check if it is an equation
        if '=' not in x:
            return None
        else:
            sysofeq.append(elabString(x))

    # create matrix and vector
    # get all the variables
    varis = {}
    for eq in eqs:
        va = re.findall("[a-z]+", eq)
        for char in va:
            varis.update({char: 0})
    listofvars = list(varis.keys())
    mat = []
    vec = []
    for eq in sysofeq:
        row = []
        for v in range(0, len(listofvars)):
            if eq.get(listofvars[v]) == None:
                row.append(0)
            else:
                row.append(eq.get(listofvars[v]))
        mat.append(row)
        vec.append(eq.get("sum"))
    # check for number of equations
    if len(listofvars) > len(mat):
        return None
    withPivot(mat, vec)
    # check if number of equations is greater than num of variables
    if len(mat) > len(mat[0]):
        for x in range(len(mat[0]), len(vec)):
            if abs(vec[x]) > 1e-6:
                return None
    # check if pivot = 0
    for pivot in range(0, len(mat[0])):
        if abs(mat[pivot][pivot]) < 1e-8:
            return None
    result = {}
    for x in range(0, len(listofvars)):

        result.update({listofvars[x]: vec[x]})
    return result


def elabString(equation):
    equation = re.sub("\+", " + ", equation)
    equation = re.sub("-", " - ", equation)
    equation = re.sub("=", " = ", equation)
    varis = {}
    allvars = re.findall("[a-z]+", equation)
    for char in allvars:
        varis.update({char: 0})
    varis.update({"sum": 0})
    leftpart = equation.split("=")[0]
    rightpart = equation.split("=")[1][1:]
    # elaborate leftparts
    leftparts = leftpart.split(" ")
    for x in range(0, len(leftparts)):
        if re.search("[a-z]+$", leftparts[x]):
            num = re.search("[0-9]*", leftparts[x]).group()
            if len(num) == 0:
                num = '1'
            if x > 0 and leftparts[x - 1] == '-':
                num = "-" + num
            curvar = (re.search("[a-z]+$", leftparts[x])).group()
            curval = varis.get(curvar)
            varis.update({re.search("[a-z]+$", leftparts[x]).group(): int(num) + curval})
        if re.search("[0-9]$", leftparts[x]):
            origval = varis.get("sum")
            if x > 0 and leftparts[x - 1] == '-':
                varis.update({"sum": origval + int(leftparts[x])})
            else:
                varis.update({"sum": origval - int(leftparts[x])})
    # elaborate rightparts
    rightparts = rightpart.split(" ")
    for x in range(0, len(rightparts)):
        if re.search("[a-z]+$", rightparts[x]):
            num = re.search("[0-9]*", rightparts[x]).group()
            if len(num) == 0:
                num = '1'
            if x > 0 and rightparts[x - 1] == '+':
                num = "-" + num
            if x == 0:
                num = "-" + num
            curvar = (re.search("[a-z]+$", rightparts[x])).group()
            curval = varis.get(curvar)
            varis.update({re.search("[a-z]+$", rightparts[x]).group(): int(num) + curval})
        if re.search("[0-9]$", rightparts[x]):
            origval = varis.get("sum")
            if x == 0:
                varis.update({"sum": origval + int(rightparts[x])})
            elif rightparts[x - 1] == '-':
                varis.update({"sum": origval - int(rightparts[x])})
            else:
                varis.update({"sum": origval + int(rightparts[x])})

    return varis


def swapRows(matrix, vector, x, y):
    rowx = matrix[x]
    matrix[x] = matrix[y]
    matrix[y] = rowx
    varx = vector[x]
    vector[x] = vector[y]
    vector[y] = varx


def addRows(matrix, x, y, mul):
    for p in range(0, len(matrix[0])):
        matrix[y][p] = matrix[y][p] - mul * matrix[x][p]


def addScalar(vector, x, y, mul):
    vector[y] = vector[y] - mul * vector[x]


def withPivot(matrix, vector):
    for r in range(0, len(matrix[0])):
        # find row number with max diagonal element
        p = [r, matrix[r][r]]
        for v in range(r, len(matrix)):
            if abs(matrix[v][r]) > abs(p[1]):
                p = [v, matrix[v][r]]
        swapRows(matrix, vector, r, p[0])
        for q in range(r + 1, len(matrix)):
            if matrix[r][r] == 0:
                return None
            mult = matrix[q][r] / matrix[r][r]
            addRows(matrix, r, q, mult)
            addScalar(vector, r, q, mult)
    for r in range(len(matrix[0]) - 1, 0, -1):
        for q in range(0, r):
            if matrix[r][r] == 0:
                return None
            mult = matrix[q][r] / matrix[r][r]
            addRows(matrix, r, q, mult)
            addScalar(vector, r, q, mult)
    for s in range(0, len(matrix[0])):
        vector[s] = vector[s] / matrix[s][s]
    return (matrix, vector)
