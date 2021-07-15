def case_unification(s):
    return s.lower() if sum(1 for i in s if i.islower()) > sum(1 for i in s if i.isupper()) else s.upper()
