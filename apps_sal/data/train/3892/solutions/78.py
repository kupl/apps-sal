def grader(score):
    if 0.7 > score >= 0.6:
        return "D"
    elif 0.8 > score >= 0.7:
        return "C"
    elif 0.9 > score >= 0.8:
        return "B"
    elif 1 >= score >= 0.9:
        return "A"
    return "F"
    

