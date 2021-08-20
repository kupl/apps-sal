def get_grade(*args):
    return {6: 'D', 7: 'C', 8: 'B', 9: 'A', 10: 'A'}.get(sum(args) // 30, 'F')
