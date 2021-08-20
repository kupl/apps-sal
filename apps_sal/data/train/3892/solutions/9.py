def grader(score):
    return ['F', 'D', 'C', 'B', 'A'][(1 >= score > 0.59) + (1 >= score >= 0.9) + (1 >= score >= 0.8) + (1 >= score >= 0.7)]
