def grader(score):
    grades="FFFFFFDCBAA"
    return grades[int(score*10)] if score <= 1 else "F"

