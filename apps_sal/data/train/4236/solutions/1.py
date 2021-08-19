def calculate_grade(scores):
    for score in scores:
        mean = sum(scores) / len(scores)
        if mean >= 90 and mean <= 100:
            return 'A'
        elif mean >= 80 and mean < 90:
            return 'B'
        elif mean >= 70 and mean < 80:
            return 'C'
        elif mean >= 60 and mean < 70:
            return 'D'
        else:
            return 'F'
