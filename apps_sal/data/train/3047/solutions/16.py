import re


def repeating_fractions(numerator, denominator):
    fracion = str(numerator / denominator).split(".")
    beforeDot = fracion[0]
    afterDot = fracion[1]
    properAfterDOT = ""
    pharenthesis = [item[0] for item in re.findall(r"((.)\2*)", afterDot)]
    for i in pharenthesis:
        if len(i) > 1:
            properAfterDOT += "(" + i[0] + ")"
        else:
            properAfterDOT += i
    return beforeDot + "." + properAfterDOT
