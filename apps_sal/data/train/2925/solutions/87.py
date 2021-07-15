def multiply(n):
    #your code here
    digits = len(list(str(n).lstrip('-')))
    return n * 5**digits
