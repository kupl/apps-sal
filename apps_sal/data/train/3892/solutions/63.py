def grader(score):
    """
    A function that takes a number as an argument and returns a grade based on that number.
    
    Score   Grade
    Anything greater than 1 or less than 0.6    "F"
    0.9 or greater  "A"
    0.8 or greater  "B"
    0.7 or greater  "C"
    0.6 or greater  "D"
    """
    
    return 'F' if score > 1 or score < .6 else {6:'D',7:'C',8:'B',9:'A',10:'A'}.get(int(score*10))

