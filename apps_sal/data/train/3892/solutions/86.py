def grader(score):
    return {6: 'D', 7: 'C', 8: 'B', 9: 'A'}.get(int(score * 10), 'F') if score != 1 else 'A'
