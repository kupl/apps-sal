def grader(score: float) -> str:
    """ Get a grade (A, B, C, D, E, F) based on given score. """
    return 'F' if score < 0.6 or score > 1 else 'A' if score >= 0.9 else 'B' if score >= 0.8 else 'C' if score >= 0.7 else 'D'
