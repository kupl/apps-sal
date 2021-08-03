import functools as ft
import math

ops = ['*', '/', '+', '-']


def SanitizeExpression(expression):
    return expression.replace("+-", "-").replace("-+", "-").replace("--", "+")
    pass


def ExtendList(arr, value, op):
    arr.extend(value.split(op))
    return arr


def LastIndexOfAny(expression, operators, startIndex):
    arr = [expression[0:startIndex].rfind(x) for x in operators]
    arr.sort()
    return arr[-1]
    pass


def IndexOfAny(expression, operators, startIndex):
    arr = [x + startIndex for x in [expression[startIndex:].find(x) for x in operators] if x != -1]
    if len(arr) == 0:
        arr = [-1]
    arr.sort()
    return arr[0]
    pass


def FloatToString(value):
    return "%.30f" % value
    pass


def EvaluateSimpleExpression(expression):
    numberText = expression.split(ops[0])
    numberText = ft.reduce(lambda r, s: ExtendList(r, s, ops[2]), numberText, [])
    numberText = ft.reduce(lambda r, s: ExtendList(r, s, ops[3]), numberText, [])
    numberText = ft.reduce(lambda r, s: ExtendList(r, s, ops[1]), numberText, [])

    numbers = [float(x) for x in numberText if x != '']

    minusCount = expression.count('-')

    if expression.count('*') > 0:
        return numbers[0] * numbers[1] * math.pow(-1, minusCount)

    if expression.count('/') > 0:
        return numbers[0] / numbers[1] * math.pow(-1, minusCount)

    if expression.count('-') > 0:
        return numbers[0] - numbers[1]

    return numbers[0] + numbers[1]
    pass


def ResolveSimpleExpression(expression, operatorIndex):
    startIndex = LastIndexOfAny(expression, ops, operatorIndex - 1) + 1
    indexNext = IndexOfAny(expression, ops, operatorIndex + 2)

    if indexNext == -1:
        length = len(expression)
    else:
        length = indexNext

    length -= startIndex

    return expression[startIndex:startIndex + length]
    pass


def EvaluateSimpleInComplexExpression(expression, operatorIndex):
    simple = ResolveSimpleExpression(expression, operatorIndex)
    simpleAns = EvaluateSimpleExpression(simple)
    if math.fabs(simpleAns) < 1e-10:
        simpleAns = 0
        pass

    insertIndex = expression.find(simple)

    return expression[0:insertIndex] + FloatToString(simpleAns) + expression[insertIndex + len(simple):]
    pass


def SimplifyExpressionByOperatorsRec(expression, applyNegative, multiplier, operators):
    if expression[0] == '+':
        expression = expression[1:]

    if applyNegative and expression[0] == '-':
        multiplier *= -1
        expression = expression[1:].replace("+", "X").replace("-", "+").replace("X", "-")
        pass

    indexArr = [x for x in [expression.find(op) for op in operators] if x > 0]
    if len(indexArr) > 0:
        indexArr.sort()
        index = indexArr[0]

        expression = EvaluateSimpleInComplexExpression(expression, index)
        expression = SanitizeExpression(expression)

        return SimplifyExpressionByOperatorsRec(expression, applyNegative, multiplier, operators)
        pass

    try:
        return FloatToString(float(expression) * multiplier)
    except:
        return expression
    pass


def SimplifyExpressionByOperators(expression, applyNegative, operators):
    return SimplifyExpressionByOperatorsRec(expression, applyNegative, 1, operators)


def EvaluateComplexExpression(expression):
    result = SimplifyExpressionByOperators(expression, False, ['*', '/'])

    return SimplifyExpressionByOperators(result, True, ['+', '-'])
    pass


def EvaluateBracketExpression(expression):
    closeIndex = expression.find(')')
    if closeIndex >= 0:
        openIndex = expression[0:closeIndex].rfind('(')
        startIndex = openIndex + 1
        length = closeIndex - startIndex

        complexExp = expression[startIndex:closeIndex]
        resolved = EvaluateComplexExpression(complexExp)

        expression = expression[0:openIndex] + str(resolved) + expression[openIndex + length + 2:]
        expression = SanitizeExpression(expression)

        return EvaluateBracketExpression(expression)
        pass

    return EvaluateComplexExpression(expression)
    pass


def calculate(expression):
    try:
        test = 'string' + expression
    except:
        return False

    expression = str(expression).replace(" ", "")
    if expression == '':
        return 0

    expression = SanitizeExpression(expression)

    try:
        return float(EvaluateBracketExpression(expression))
    except:
        return False
    pass
