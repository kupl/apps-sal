def final_grade(e, p):
    return [100, 90, 75, 0][0 if(e > 90 or p > 10)else 1 if(e > 75 and p > 4)else 2 if (e > 50 and p > 1)else 3]
