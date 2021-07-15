def array_madness(a,b):
    result_a = 0
    result_b = 0
    for i in a:
        result_a += i ** 2
    for i in b:
        result_b += i ** 3
    return True if result_a > result_b else False

