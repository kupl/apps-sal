def final_grade(e, p): return 100 * (e > 90 or p > 10) or 90 * (e > 75 and p > 4) or 75 * (e > 50 and p > 1)
