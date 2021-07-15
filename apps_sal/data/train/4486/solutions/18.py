def repeat_it(string,n):
     return "Not a string" if type(string) != str else ''.join([string for i in range (1, n + 1)])
