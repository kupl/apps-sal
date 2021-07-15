def final_grade(exm, prj):
    if exm > 90 or prj > 10:
        return 100
    if exm > 75 and prj >= 5:
        return 90
    if exm > 50 and prj >= 2:
        return 75
    return 0
