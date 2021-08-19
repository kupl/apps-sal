def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    scale = {'A': 90 <= avg <= 100, 'B': 80 <= avg < 90, 'C': 70 <= avg < 80, 'D': 60 <= avg < 70, 'F': 0 <= avg < 60}
    for (k, v) in scale.items():
        if v == True:
            return k
