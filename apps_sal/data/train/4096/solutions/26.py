# Write a function called that takes a string of parentheses, and determines
# if the order of the parentheses is valid. The function should return true
# if the string is valid, and false if it's invalid.
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints: 0 <= input.length <= 100
# Along with opening (() and closing ()) parenthesis, input may contain
# any valid ASCII characters. Furthermore, the input string may be empty
# and/or not contain any parentheses at all. Do not treat other forms
# of brackets as parentheses (e.g. [], {}, <>).

def valid_parentheses(string):
    str = string
    if str == "":
        return True
    if len(str) > 100:
        str = str[0:100]
    c_open = 0
    exc = 0
    for c in str:
        if c == '(':
            c_open += 1
        if c == ')':
            c_open -= 1
            if c_open < 0:
                exc = 1
                break
    if exc == 1 or c_open != 0:
        return False
    return True
