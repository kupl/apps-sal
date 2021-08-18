def calculate_age(yob, cy):
    if yob < cy:
        if (cy - yob) == 1:
            return f"You are {cy-yob} year old."
        return f"You are {cy-yob} years old."
    elif yob > cy:
        if (yob - cy) == 1:
            return f"You will be born in {yob-cy} year."
        return f"You will be born in {yob-cy} years."
    else:
        return "You were born this very year!"
