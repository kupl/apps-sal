def get_grade(s1,
              s2,
              s3):

    score = s1 + s2 + s3
    if (270 <= score):

        return "A"

    elif (240 <= score):

        return "B"

    elif (210 <= score):

        return "C"

    elif (180 <= score):

        return "D"

    return "F"

