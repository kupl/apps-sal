GRADES_MAP = {6: 'D', 7: 'C', 8: 'B', 9: 'A'}


def grader(s):
    return GRADES_MAP.get(int(s * 10), 'A' if s == 1 else 'F')
