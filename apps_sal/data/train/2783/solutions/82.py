def get_grade(*args):
    if sum(args) / len(args) >= 90:
        return 'A'
    if sum(args) / len(args) >= 80:
        return 'B'
    if sum(args) / len(args) >= 70:
        return 'C'
    if sum(args) / len(args) >= 60:
        return 'D'
    return 'F'
