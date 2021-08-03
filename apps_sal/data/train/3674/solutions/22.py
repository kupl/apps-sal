def add_binary(a, b):
    ans = a + b
    result = ""
    while ans != 0:
        result += str(ans % 2)
        ans = ans // 2
    return result[::-1]
