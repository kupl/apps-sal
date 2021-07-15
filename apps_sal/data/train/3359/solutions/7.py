title_to_number = lambda a: 0 if a == '' else 1 + ord(a[-1]) - ord('A') + 26 * title_to_number(a[:-1])
