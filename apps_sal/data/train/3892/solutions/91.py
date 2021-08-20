def grader(score):
    fixed = int(score * 10)
    dict = {6: 'D', 7: 'C', 8: 'B', 9: 'A'}
    return dict.get(fixed, 'F') if score != 1 else 'A'
