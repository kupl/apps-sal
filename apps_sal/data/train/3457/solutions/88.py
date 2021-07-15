def final_grade(e, p):
    if e>90 or p>10:
        return 100
    if 75<e<=90 and p>=5 and p<=10:
        return 90
    if 50<e<=90 and p>=2 and p<=10:
        return 75
    else:
        return 0
