def zeros(n):
    final = 0
    if n == 0:
        return 0
    for x in range(1, 15):
        final += n // 5**x
    print(final)
    return final

    

