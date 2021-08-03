def repeater(string, n):
    result = ""
    while(n != 0):
        result += string
        n -= 1
    return result
