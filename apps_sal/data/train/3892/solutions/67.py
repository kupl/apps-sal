def grader(score):
       if score > 1 or score < 0.6:
           return 'F'
       if score == 0.9:
           return 'A'
       if score == 0.8:
           return 'B'
       if score == 0.7:
           return 'C'
       if score == 0.6:
           return 'D'
       return 'A'
