def final_grade(exam, projects):
    array=[100,90,75,0]
    if exam>90 or projects>10:
        return array[0]
    elif exam>75 and projects>=5:
        return array[1]
    elif exam>50 and projects>=2:
        return array[2]
    else:
        return array[3]
