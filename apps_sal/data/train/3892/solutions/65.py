def grader(score):
    if score <= 1 and score >= 0.9:
        return "A"
    elif score < .9 and score >= 0.8:
        return "B"
    elif score < .8 and score >= 0.7:
        return "C"
    elif score < .7 and score >= 0.6:
        return "D"
    else:
        return "F"
