import re
from fractions import Fraction


def solve(*equations):
    equations2 = []
    for x in equations:
        equations2.append(x)
    equations = equations2

    def parsing(equations):
        vectconstant = []
        matrixcoefficient = []
        listvariables = []
        for equation in equations:
            eqvariables = re.findall('[A-Za-z]+', equation)
            listvariables = listvariables + eqvariables
        listvariables = list(set(listvariables))
        for equation in equations:
            listcoefficient = []
            equation = re.sub('\\s', '', equation)
            eqdivided = equation.split('=')
            (firstp, secondp) = (eqdivided[0], eqdivided[1])
            constantterm1 = re.findall('[\\-\\+]*\\d+\\.?\\d*(?=[+-])|[\\-\\+]*\\d+\\.?\\d*$', firstp)
            constantterm2 = re.findall('[\\-\\+]*\\d+\\.?\\d*(?=[+-])|[\\-\\+]*\\d+\\.?\\d*$', secondp)
            for x in range(len(constantterm1)):
                constantterm1[x] = '-' + constantterm1[x]
                constantterm1[x] = re.sub('\\+\\+|\\-\\-', '+', re.sub('\\+\\-|\\-\\+', '-', constantterm1[x]))
            constantterm = Fraction(sum(list(map(float, constantterm1 + constantterm2))))
            vectconstant.append(constantterm)
            for x in listvariables:
                values1 = re.findall('([\\-\\+]*[\\d.]*)' + re.escape(x) + '(?=[+-]|$)', firstp)
                values2 = re.findall('([\\-\\+]*[\\d.]*)' + re.escape(x) + '(?=[+-]|$)', secondp)
                for x in range(len(values2)):
                    values2[x] = '-' + values2[x]
                    values2[x] = re.sub('\\+\\+|\\-\\-', '+', re.sub('\\+\\-|\\-\\+', '-', values2[x]))
                values = values1 + values2
                for x in range(len(values)):
                    if values[x] == '' or values[x] == '+':
                        values[x] = '1'
                    elif values[x] == '-':
                        values[x] = '-1'
                    values[x] = float(values[x])
                coefficient = Fraction(sum(values))
                listcoefficient.append(coefficient)
            matrixcoefficient.append(listcoefficient)
        return (matrixcoefficient, vectconstant, listvariables)

    def eliminateuselessrows(matrixcoefficient, vectconstant):
        (newmatrix, newvector) = ([], [])
        for (t, x) in enumerate(matrixcoefficient):
            for y in x:
                if y != Fraction(0, 1):
                    (newmatrix.append(x), newvector.append(vectconstant[t]))
                    break
        return (newmatrix, newvector)

    def GaussReduction(matrixcoefficient, vectconstant):
        c = 0
        while c < min(len(matrixcoefficient[0]), len(matrixcoefficient)):
            if matrixcoefficient[c][c] == Fraction(0, 1):
                for (t, x) in enumerate(matrixcoefficient):
                    if matrixcoefficient[t][c] != Fraction(0, 1):
                        (matrixcoefficient[c], matrixcoefficient[t]) = (matrixcoefficient[t], matrixcoefficient[c])
                        (vectconstant[c], vectconstant[t]) = (vectconstant[t], vectconstant[c])
            for (t, x) in enumerate(matrixcoefficient):
                factor = x[c]
                if t > c and matrixcoefficient[c][c] != Fraction(0, 1):
                    vectconstant[t] = vectconstant[t] - vectconstant[c] * factor / matrixcoefficient[c][c]
                    for (s, y) in enumerate(x):
                        matrixcoefficient[t][s] = y - matrixcoefficient[c][s] * factor / matrixcoefficient[c][c]
            (matrixcoefficient, vectconstant) = eliminateuselessrows(matrixcoefficient, vectconstant)
            c = c + 1
        return (matrixcoefficient, vectconstant)
    (matrixcoefficient, vectconstant, listvariables) = parsing(equations)
    (matrixcoefficient, vectconstant) = GaussReduction(matrixcoefficient, vectconstant)
    (rk1, rk2) = (0, 0)
    for (t, x) in enumerate(matrixcoefficient):
        for y in x:
            if y != Fraction(0, 1):
                rk1 = rk1 + 1
                rk2 = rk2 + 1
                break
        else:
            if vectconstant[t] != Fraction(0, 1):
                rk2 = rk2 + 1
    if rk1 < rk2:
        return None
    if rk1 == rk2 < len(listvariables):
        return None
    (matrixcoefficient, vectconstant) = eliminateuselessrows(matrixcoefficient, vectconstant)
    for x in matrixcoefficient:
        x.reverse()
    (matrixcoefficient.reverse(), vectconstant.reverse(), listvariables.reverse())
    (matrixcoefficient, vectconstant) = GaussReduction(matrixcoefficient, vectconstant)
    for (t, x) in enumerate(matrixcoefficient):
        vectconstant[t] = vectconstant[t] * (1 / x[t])
    dictsolutions = {}
    for (t, x) in enumerate(vectconstant):
        dictsolutions.update({listvariables[t]: float(vectconstant[t])})
    return dictsolutions
