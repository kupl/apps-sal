def title_to_number(a):
    return 0 if a == '' else 1 + ord(a[-1]) - ord('A') + 26 * title_to_number(a[:-1])
