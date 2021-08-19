def grader(s):
    return s > 1 and 'F' or (0.9 <= s <= 1 and 'A') or (0.8 <= s < 0.9 and 'B') or (0.7 <= s < 0.8 and 'C') or (0.6 <= s < 0.7 and 'D') or (s < 0.6 and 'F')
