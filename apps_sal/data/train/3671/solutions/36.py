def problem(a):
    print(a)
    return 'Error' if isinstance(a, str) else 50 * a + 6
