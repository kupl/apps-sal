def grader(s):
    return (s > 1 or s < 0.6) and 'F' or chr(ord('A') + int(9 - s * 10 + 0.5))
