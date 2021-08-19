def grader(score):
    return {score < 0.6 or score > 1: 'F', score >= 0.6 and score < 0.7: 'D', score >= 0.7 and score < 0.8: 'C', score >= 0.8 and score < 0.9: 'B', score >= 0.9 and score <= 1: 'A'}[True]
