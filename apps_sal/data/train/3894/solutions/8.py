def solve(s):
    counter = 0
    for char in s:
        if char.isupper():
            counter += 1
    print(counter)
    return s.lower() if counter <= len(s) / 2 else s.upper()
