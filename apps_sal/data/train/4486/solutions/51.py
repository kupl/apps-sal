def repeat_it(string, n):
    # your code here
    try:
        a = string.lower()
        return string * n
    except:
        return 'Not a string'
