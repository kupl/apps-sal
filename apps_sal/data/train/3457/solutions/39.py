#def final_grade(e, p):
#    return [0, 75, 90, 100][(e>90 and p>10) + (e>75 and p>=5) + (e>50 and p>=2)]

final_grade = lambda e, p: [0, 75, 90, 100, 100, 100][(e>90 or p>10)*3 + (e>75 and p>=5) + (e>50 and p>=2)]
