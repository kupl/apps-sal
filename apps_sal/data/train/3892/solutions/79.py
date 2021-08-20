def grader(score):
    return 'D' if score >= 0.6 and score < 0.7 else 'C' if score >= 0.7 and score < 0.8 else 'B' if score >= 0.8 and score < 0.9 else 'A' if score >= 0.9 and score <= 1 else 'F'
