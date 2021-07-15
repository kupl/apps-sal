def grader(score):
    return ('F', 'D', 'C', 'B', 'A')[(score <= 1) * ((score >= 0.6) + (score >= 0.7) + (score >= 0.8) + (score >= 0.9))]
