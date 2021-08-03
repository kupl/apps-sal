def pattern(n):
    result = ""
    if n < 1:
        return ""
    else:
        for num in range(1, n + 1):
            row = ''
            for x in range(0, num):
                row += str(num)
            result += row
            if num < n:
                result += '\n'
            else:
                pass
    return result
