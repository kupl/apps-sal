def calculate_age(birth, current):
    total = abs(current - birth)
    plural = 's' if total > 1 else ''
    if birth == current:
        return "You were born this very year!"
    return "You will be born in {} year{}.".format(total, plural) if birth > current else "You are {} year{} old.".format(total, plural)
