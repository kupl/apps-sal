def pattern(n):
    val = []
    result = ''
    if n < 1:
        return ''
    else:
        val.append(str(1))
        print(val)
        for num in range(2, n + 1):
            s = str(num) * num
            val.append('\n' + s)
    return result.join(val)
