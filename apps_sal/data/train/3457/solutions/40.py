def final_grade(s, p):
    return 100 if s>90 or p>10 else 90 if s>75 and p>=5 else 75 if s>50 and p>=2 else 0  
