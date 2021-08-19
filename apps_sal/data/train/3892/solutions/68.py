def grader(score):
    return {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}.get(int(score * 10), 'F') if score <= 1 else 'F'
