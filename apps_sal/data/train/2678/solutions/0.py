def no_order(equation):
    equation = equation.replace(' ', '')
    equation = equation.replace('+', ')+')
    equation = equation.replace('-', ')-')
    equation = equation.replace('*', ')*')
    equation = equation.replace('/', ')//')
    equation = equation.replace('%', ')%')
    equation = equation.replace('^', ')**')
    equation = '('*equation.count(')') + equation
    try : return eval(equation)
    except : pass
