def get_grade(s1, s2, s3):
    return next('ABCDF'[i] for i, low in enumerate([90, 80, 70, 60, 0]) if (s1 + s2 + s3) / 3 >= low)
