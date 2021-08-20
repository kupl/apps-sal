def animals(heads, legs):
    a = heads - (legs // 2 - heads)
    b = legs // 2 - heads
    return 'No solutions' if legs % 2 or a < 0 or b < 0 else (a, b)
