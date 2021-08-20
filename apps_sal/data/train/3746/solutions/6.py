def next_pal(val):
    val += 1
    while f'{val}' != f'{val}'[::-1]:
        val += 1
    return val
